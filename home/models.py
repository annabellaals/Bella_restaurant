import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from home.manager import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    username = None
    objects = UserManager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField("email address", blank=False, null=False, unique=True)
    address = models.TextField(blank=True, null=True, default="")
    phone = models.TextField(blank=True, null=True, default="")
    is_phone_verified = models.BooleanField(default=False)
    city = models.TextField(blank=True, null=True, default="")
    state = models.TextField(blank=True, null=True, default="")
    country = models.TextField(blank=True, null=True, default="Sweden")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class FoodType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return self.image.url

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
        }


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class OrderStatus(models.TextChoices):
        VERIFIED = 'VERIFIED', _('VERIFIED')
        PREPARING = 'PREPARING', _('PREPARING')
        DELIVERING = 'DELIVERING', _('DELIVERING')
        DELIVERED = 'DELIVERED', _('DELIVERED')
        REJECTED = 'REJECTED', _('REJECTED')
        CANCELLED = 'CANCELLED', _('CANCELLED')

    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.VERIFIED)
    comments = models.TextField(blank=True, null=False, default="")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def order_amount(self):
        order_items = OrderFood.objects.filter(order=self)
        total_price = 0
        for order_item in order_items:
            total_price += order_item.food.price
        return total_price


class OrderFood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class TableBooking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_name = models.CharField(max_length=200)
    booking_phone = models.CharField(max_length=50)
    booking_date = models.DateTimeField()
    people = models.PositiveIntegerField(default=1)
    message = models.CharField(max_length=500)

    class BookStatus(models.TextChoices):
        PENDING = 'PENDING', _('PENDING')
        BOOKED = 'BOOKED', _('BOOKED')
        CANCELED = 'CANCELED', _('CANCELED')

    status = models.CharField(
        max_length=20, choices=BookStatus.choices, default=BookStatus.PENDING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
