from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('cart/', views.cart, name="cart"),
    path('account/', views.account, name="account"),
    path('manager-account/', views.manager_account, name="manager-account"),
    path('manager-save-order/', views.manager_save_order, name="manager-save-order"),
    path('manager_save_booking/', views.manager_save_booking, name="manager-save-booking"),
    path('cart/ajax/place_order/', views.place_order, name='place_order'),
    path('book/ajax/check-table-availability/', views.check_table_availability, name='check-table-availability'),
]