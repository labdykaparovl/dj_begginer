from django.contrib import admin

from .models import Item, Purchase
from catalog.models import Category, Product

admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(Category)
admin.site.register(Product)



