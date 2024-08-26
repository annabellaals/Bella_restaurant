from django.contrib import admin

from home.models import User, Food, FoodType, Order, TableBooking


admin.site.register(User)
admin.site.register(Food)
admin.site.register(FoodType)
admin.site.register(Order)
admin.site.register(TableBooking)