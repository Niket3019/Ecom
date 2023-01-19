from django.shortcuts import render,HttpResponse
from .models import Product
from .catergory import Catergory
from .models import Register_Customer
from django.contrib.auth.models import User,auth 
import re


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
# Template Link
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
    
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        fullname = postData.get('fullname')
        emailaddress = postData.get('emailaddress')
        phone = postData.get('phone')
        password = postData.get('password')
        confirmpassword = postData.get('confirmpassword')
        # validation
        error_message = None
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (username and fullname and emailaddress and phone and password and confirmpassword):
            error_message = "This Field Is Required !!"
        elif len(fullname)<4:
            error_message = "Full Name Must Be 4 Char Long "
        if re.match(regex,emailaddress):
                print(True)
        else:
           error_message = "The Given Email Input Is Not Valid"
       
           
                

        # end of validation
        if not error_message:
               print(username,phone,emailaddress,password)
        # save the data in admin
               customer = Register_Customer( username = username,
               fullname = fullname,
               emailaddress = emailaddress,
               phone = phone, password = password, 
               confirmpassword = confirmpassword )

               customer.save()
        # end of save
        else:
          return render(request,'chairapp/register.html',{'error':error_message})
    else:
        return render(request,'chairapp/register.html')
