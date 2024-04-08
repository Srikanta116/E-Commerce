from django.contrib import admin
from app.models import Product, Customer, Cart, OrderPlaced
# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(OrderPlaced)

