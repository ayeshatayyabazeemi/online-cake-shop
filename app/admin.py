from django.contrib import admin
from .models import Products, UserInfo, Order, OrderDetail  # Add other models

admin.site.register(Products)
admin.site.register(UserInfo)
admin.site.register(Order)
admin.site.register(OrderDetail)

# Register your models here.
