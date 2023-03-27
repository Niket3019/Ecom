from django.shortcuts import render,redirect
from chairapp.models import Register_Customer
from django.contrib.auth.hashers import make_password
import re
from django.views import View


class register(View):
    def get(self,request):
         return render(request,'chairapp/register.html')
    def post(self,request):
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
        error_message = self.ValidateRegisterUser(customer)
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
    
    def ValidateRegisterUser(self,customer):
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
        elif len(customer.phone)<10:
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
