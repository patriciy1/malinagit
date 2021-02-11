from django.contrib import admin
from .models import Product,Customer, ShippingAddress, Order, OrderItem, Category

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)