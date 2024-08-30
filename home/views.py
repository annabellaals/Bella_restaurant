import json
from datetime import datetime

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import User, Food, FoodType, Order, OrderFood, TableBooking, ReservationTables
from home.utils import get_available_tables


def home(request):
    if request.user.groups.filter(name="manager").exists():
        return redirect('manager-account')
    context = {'is_authenticated': request.user.is_authenticated,
               'user': request.user,
               'foods': Food.objects.filter(available=True),
               'food_types': FoodType.objects.all(),
                'manager': False
               }
    return render(request, 'home/index.html', context)


def about(request):
    if request.user.groups.filter(name="manager").exists():
        return redirect('manager-account')
    context = {'is_authenticated': request.user.is_authenticated,
               'user': request.user
               }
    return render(request, 'home/about.html', context)



def book(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.groups.filter(name="manager").exists():
        return redirect('manager-account')

    context = {'is_authenticated': request.user.is_authenticated,
               'user': request.user
               }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        people = request.POST.get('people')

        date_string = request.POST.get('date-picker') + " " + request.POST.get('time-picker')
        format_string = "%Y-%m-%d %I:%M %p"
        reservation_datetime = datetime.strptime(date_string, format_string)
        table_id = request.POST.get('table-picker')
        table = ReservationTables.objects.filter(table_id=table_id)

        message = request.POST.get('message')

        TableBooking.objects.create(user=request.user,
                                    booking_name=name,
                                    booking_phone=phone,
                                    people=people,
                                    booking_date=reservation_datetime,
                                    message=message,
                                    reservation_table=table.first()
                                    )
        return redirect('account')
    return render(request, 'home/book.html', context)


def menu(request):
    if request.user.groups.filter(name="manager").exists():
        return redirect('manager-account')
    context = {
        'is_authenticated': request.user.is_authenticated,
        'user': request.user,
        'foods': Food.objects.filter(available=True),
        'food_types': FoodType.objects.all(),
    }
    return render(request, 'home/menu.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name="manager").exists():
                return redirect('manager-account')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    else:
        list(messages.get_messages(request))
    return render(request, 'home/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please try login.")
            return render(request, 'home/register.html')

        if password != password1:
            messages.error(request, "Both Passwords is not same. Please try again.")
            return render(request, 'home/register.html')

        user = User.objects.create_user(email, password1)
        user.first_name = first_name
        user.phone = phone
        user.save()
        login(request, user)
        return redirect('home')

    else:
        storage = messages.get_messages(request)
        for _ in storage:
            pass

    return render(request, 'home/register.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def cart(request):
    if request.user.groups.filter(name="manager").exists():
        return redirect('manager-account')

    context = {'is_authenticated': request.user.is_authenticated,
               'user': request.user
               }
    return render(request, 'home/cart.html', context)


def account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.groups.filter(name="manager").exists():
        return redirect('manager-account')

    context = {'is_authenticated': request.user.is_authenticated,
               'user': request.user,
               'orders': Order.objects.filter(user=request.user).prefetch_related('orderfood_set'),
               'bookings': TableBooking.objects.filter(user=request.user)
               }
    return render(request, 'home/account.html', context)


def place_order(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'redirect': "/login"}), content_type="application/json")

    if request.user.groups.filter(name="manager").exists():
        return HttpResponse(json.dumps({'redirect': "/manager-account"}), content_type="application/json")

    if request.method != 'POST':
        return HttpResponse(json.dumps({'redirect': "/home"}), content_type="application/json")

    data = json.loads(request.body)
    ids = data.get("item_ids", [])
    foods = []
    for item_id in ids:
        food = Food.objects.filter(pk=item_id).first()
        if food:
            foods.append(food)

    if not foods:
        return HttpResponse(json.dumps({'redirect': "/menu"}), content_type="application/json")

    order = Order.objects.create(user=request.user)
    for food in foods:
        OrderFood.objects.create(order=order, food=food)

    return HttpResponse(json.dumps({'redirect': "/account"}), content_type="application/json")


def manager_account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.groups.filter(name="manager").exists():
        return redirect('home')

    context = {'is_authenticated': request.user.is_authenticated,
               'user': request.user,
               'orders': Order.objects.all().prefetch_related('orderfood_set'),
               'bookings': TableBooking.objects.all(),
               'oder_options': Order.OrderStatus,
               'booking_options': TableBooking.BookStatus
               }

    return render(request, 'home/manager/account.html', context)


def manager_save_order(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    if not request.user.groups.filter(name="manager").exists():
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    if request.method != 'POST':
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    data = json.loads(request.body)
    order = Order.objects.filter(pk=data.get('order_id')).first()
    if not order:
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")
    order.status = data.get('selected_value')
    order.comments = data.get('comment_value')
    order.save()
    return HttpResponse(json.dumps({'response': True}), content_type="application/json")


def manager_save_booking(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    if not request.user.groups.filter(name="manager").exists():
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    if request.method != 'POST':
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    data = json.loads(request.body)
    table_booking = TableBooking.objects.filter(pk=data.get('booking_id')).first()
    if not table_booking:
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")
    table_booking.status = data.get('selected_value')
    table_booking.save()
    return HttpResponse(json.dumps({'response': True}), content_type="application/json")


def check_table_availability(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    if request.user.groups.filter(name="manager").exists():
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    if request.method != 'POST':
        return HttpResponse(json.dumps({'response': False}), content_type="application/json")

    data = json.loads(request.body)
    tables = get_available_tables(data.get('date_value'),data.get('time_value'))
    return HttpResponse(json.dumps({'response': True, 'tables':tables}), content_type="application/json")
