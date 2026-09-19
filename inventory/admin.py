from django.contrib import admin
from .models import Category, Product

#registering models for admin

admin.site.register(Category)
admin.site.register(Product)
