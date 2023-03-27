from django.shortcuts import render,redirect,HttpResponse
from .models import Product,Track_User_Path,count_button_click,VedioDuration
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
import requests
from django.core.cache import cache
from .catergory import Catergory
from django.views import View
from chairapp.models import Register_Customer,NewPassCreate
from .token import send_forget_password_mail
import uuid
# Create your views here.

# Create your views here.
api_key = '59112e83bad64742ba80769e43a26647'

api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key

 

def get_ip_geolocation_data(ip_address):

   # not using the incoming IP address for testing

   print(ip_address)

   print('saving ip')

   response = requests.get(api_url)
   print(response.content)
   return response.content

   

def teck_pages(request):
    print('going1')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   
    if x_forwarded_for:

                ip = x_forwarded_for.split(',')[0]
                
    else:

                 ip = request.META.get('REMOTE_ADDR')
                 
                 
    geolocation_json = get_ip_geolocation_data(ip)

    geolocation_data = json.loads(geolocation_json)

    country = geolocation_data['country']

    region = geolocation_data['region']  
    user_ip = ip 
  
    now = datetime.datetime.now()
   
    visited_pages = request.session.get('visited_pages', [])
    
    if user_ip in cache:
               
               print("chache",cache)
               last_access_time = cache.get(user_ip)
        # Calculate the duration of the user's visit
               duration = now - last_access_time
        # Update the cached access time to the current time
               cache.set(user_ip, now)

    else:
        # If the user's IP address is not in the cache, store the current time
                   cache.set(user_ip, now)
                   duration = datetime.timedelta(0)
    visited_pages.append(request.path)

    request.session['visited_pages'] = visited_pages
    page_view = Track_User_Path(ip_address=user_ip, url=request.path, duration=duration,region=region,country=country,date_time=now)
    page_view.save()

@csrf_exempt
def count_button_video_duration(request):
    if request.method == 'POST':
        ip = request.META.get('REMOTE_ADDR')
        tag_name = request.POST.get('button_id')
        click_count = request.POST.get('count')
        if tag_name is not None:
         button_click = count_button_click(tag_name=tag_name, click_count=click_count,ip_address=ip)
         button_click.save()
        else:
             ip = request.META.get('REMOTE_ADDR')
             data = json.loads(request.body.decode('utf-8'))
             start_time = data['start_time']
             pause_time = data['duration']
             duration = data['duration']
             total_duration = data['total_duration']
             video_view = VedioDuration(start_time=start_time, pause_time=pause_time,duration=duration,total_duration=total_duration,ip_address=ip)
             video_view.save()
             return 'success'                                                                                          
    return 'okok'                             
  
class Home(View):
  def post(self,request):
      product = request.POST.get('product')
      cart = request.session.get('cart')
      if cart:
          quantity = cart.get(product)
          if quantity:
            cart[product] = quantity+1
          else:
              cart[product] = 1
      else:
          cart = {}
          cart[product] = 1
      request.session['cart'] = cart
      print('cart:',request.session['cart'])
      return redirect('HomePage')
  def get(self,request):
    print('ip coming')
    # cart check
    cart = request.session.get('cart')
    if not cart:
         request.session.cart = {}
    # end cart check
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
    print(request.session.get('customer_email'))
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
    try:
     if request.method == 'POST':
          emailaddress = request.POST.get('emailaddress')
          if not Register_Customer.objects.filter(emailaddress = emailaddress):
               error_message = "Email Not Exist !!"
               return render(request,'chairapp/forgot.html',{'error':error_message})
          forgot_password = Register_Customer.objects.get(emailaddress = emailaddress)
          print(forgot_password)
          token = str(uuid.uuid4())
          print(token)
          forgetpass = NewPassCreate.objects.get(emailaddress=forgot_password)
          forgetpass.forgot_password_token = token
          forgetpass.save()
          send_forget_password_mail(forgot_password , token)
          error_message = "Email is sent to emailaddress !!"
          return render(request,'chairapp/forgot.html',{'error':error_message})         
    except Exception  as e:
        print(e)
    return render(request,'chairapp/forgot.html')
def createpassword(request,token):
    context = {}
    try:
         forgetpass = NewPassCreate.objects.get(forgot_password_token = token)
         print('okok',forgetpass)
         
    except Exception as e:
         print(e)
    return render(request,'chairapp/createpassword.html')
def tnc(request):
    return render(request,'chairapp/tnc.html')

      
