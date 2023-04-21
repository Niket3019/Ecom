from django.shortcuts import render
from chairapp.models import Register_Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from chairapp.views import teck_pages,count_button_click

class Login(View):
    def get(self,request):
               teck_pages(request)
               return render(request,'chairapp/login.html')

    def post(self,request):
        teck_pages(request)
        postData = request.POST
        emailaddress = postData.get('emailaddress')
        password = postData.get('password')
        register_customer_emailaddress = Register_Customer.get_customer_by_email(emailaddress)
        print('---------->getting',register_customer_emailaddress)
        error_message = None
        if register_customer_emailaddress:
            flag = check_password(password,register_customer_emailaddress.password)
            print('------------------------------------>>',register_customer_emailaddress.password)
            if flag:
                request.session['customer_id'] = register_customer_emailaddress.id
                request.session['customer_email'] = register_customer_emailaddress.emailaddress
                return render(request,'chairapp/HomePage.html',{'emailaddress':emailaddress})
                
            else:
                error_message = "Username/Email Or Password Are Invalid !!"
        else:
             error_message = "Username/Email Or Password Are Invalid !!"
        return render(request,'chairapp/login.html',{'error':error_message})

