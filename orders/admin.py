# from django.contrib import admin
# from orders.models import *
# # Register your models here.
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'status_code', 'description', 'created', 'modified']
#     exclude = ('modified',)
#
#
# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order', 'product', 'quantity', 'created', 'modified']
#     exclude = ('modified',)
#
#
# @admin.register(OrderStatusCode)
# class OrderStatusCodeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'created', 'modified']
#     exclude = ('modified',)
#
#
# @admin.register(CartItem)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product', 'quantity', 'created', 'modified']
#     exclude = ('modified',)
