from django.contrib import admin

# Register your models here.
from .models import Product
from .catergory import Catergory

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','catergory']

class AdminCatergory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product,AdminProduct)
admin.site.register(Catergory,AdminCatergory)