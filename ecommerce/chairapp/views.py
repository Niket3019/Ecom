from django.shortcuts import render,HttpResponse,redirect
from .models import Product
from .catergory import Catergory
from .models import Register_Customer
from django.contrib.auth.models import User,auth 
from django.contrib.auth.hashers import make_password,check_password
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
def ValidateRegisterUser(customer):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        error_message = None
        if not customer.username:
            error_message = "Username Is Required !!"
        elif customer.EmailisExist():
            error_message = "Email Address Already Exit"
        elif customer.PhoneisExist():
            error_message = "Phone Number Alredy Exist"
        elif customer.UsernameisExist():
            error_message = "Username Already Exit"
        elif len(customer.fullname)<4:
            error_message = "Full Name Must Be 4 Char Long "
        elif not customer.phone:
            error_message = "Phone Number Required !!"
        elif len(customer.phone)==11:
            error_message = "Phone Must Be 10 Char Long"
        elif customer.password != customer.confirmpassword:
            error_message = "The Password Is Not Same"
        elif re.match(regex,customer.emailaddress):
            pass
        elif not customer.emailaddress:
            error_message = "Email Input Is Not Valid"     
        else:
            error_message =  "Email Should Correct"   
        return error_message  
def registeruserpost(request):
        postData = request.POST
        username = postData.get('username')
        fullname = postData.get('fullname')
        emailaddress = postData.get('emailaddress')
        phone = postData.get('phone')
        password = postData.get('password')
        confirmpassword = postData.get('confirmpassword')
        value = {
            'username' : username, 'fullname': fullname,'emailaddress': emailaddress,
            'phone':phone,'password':password,'confirmpassword':confirmpassword
        }
        customer = Register_Customer( username = username,
               fullname = fullname,
               emailaddress = emailaddress,
               phone = phone, password = password, 
               confirmpassword = confirmpassword )
        error_message = ValidateRegisterUser(customer)
        # validation
         
        # end of validation
        if not error_message:
               print(username,phone,emailaddress,password)
        # Hashingh Password
               customer.password = make_password(customer.password)
        # save the data in admin
               customer.save()
        # end of save
               return redirect("HomePage")

        else:
           data ={
            'error':error_message,
            'values':value
           }
        return render(request,'chairapp/register.html',data)
def register(request):
      if request.method == 'GET':
        return render(request,'chairapp/register.html')
      else:
       return registeruserpost(request)
def login(request):
    if request.method == 'GET':
       return render(request,'chairapp/login.html')
    else:
        postData = request.POST
        emailaddress = postData.get('emailaddress')
        password = postData.get('password')
        register_customer_emailaddress = Register_Customer.get_customer_by_email(emailaddress)
        
        error_message = None
        if register_customer_emailaddress:
            flag = check_password(password,register_customer_emailaddress.password)
            if flag:
                return redirect('HomePage')
            else:
                error_message = "Username/Email Or Password Are Invalid !!"
        else:
             error_message = "Username/Email Or Password Are Invalid !!"
        return render(request,'login.html',{'error':error_message})
