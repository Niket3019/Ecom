from django.shortcuts import render
from .models import Product
from .catergory import Catergory
# Create your views here.
def HomePage(request):
    products = None
    catergories = Catergory.get_all_categories()
    catergoryId = request.GET.get('catergory')
    if catergoryId:
       products = Product.get_all_products_by_catergoryid(catergoryId)
    else:
         products = Product.get_all_products()
    data = {}
    data['catergories'] = catergories
    data['products'] = products
    return render(request,'chairapp/HomePage.html', data)
def about(request):
    return render(request,'chairapp/about.html')
def login(request):
    return render(request,'chairapp/login.html')
def why(request):
    return render(request,'chairapp/why.html')
def product(request):
        
    return render(request,'chairapp/product.html')
def testimonial(request):
    return render(request,'chairapp/testimonial.html')
def forgot(request):
    return render(request,'chairapp/forgot.html')
def tnc(request):
    return render(request,'chairapp/tnc.html')
def register(request):
    return render(request,'chairapp/register.html')

