from django.contrib import admin

# Register your models here.

from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]
    list_filter = ["name"]

