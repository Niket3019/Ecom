from django.contrib import admin

# Register your models here.
from .models import Product,ReviewRating
from .catergory import Catergory
from .models import Register_Customer,Track_User_Path,count_button_click,VedioDuration,order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','catergory']

class AdminCatergory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product,AdminProduct)
admin.site.register(Catergory,AdminCatergory)
admin.site.register(Register_Customer)

admin.site.register(Track_User_Path)
admin.site.register(count_button_click)
admin.site.register(VedioDuration)
admin.site.register(ReviewRating)
admin.site.register(order)