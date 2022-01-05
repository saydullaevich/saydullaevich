from django.contrib import admin
from .models import Products


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'rasm']

admin.site.register(Products, ProductAdmin)