from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Product,Track_User_Path,count_button_click,VedioDuration
from django.http import HttpResponseRedirect
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from chairapp.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator
import requests
from django.core.cache import cache
from .catergory import Catergory
from django.views import View
from chairapp.models import Register_Customer,Product,ReviewRating,order
from .token import send_forget_password_mail
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg,Count
from .forms import ReviewForm,ReviewRating
from django.contrib import messages
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
    if 'country' in geolocation_data:
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
  @csrf_exempt
  def post(self,request):
      count_button_video_duration(request)
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
    teck_pages(request)
    print('ip coming')
    # cart check
    cart = request.session.get('cart')
    if not cart:
         request.session.cart = {}
    # end cart check
    products = None
    catergories = Catergory.get_all_categories()
    catergoryId = request.GET.get('catergory')
    print('------>',catergoryId,catergories)
    if catergoryId:
       products = Product.get_all_products_by_catergoryid(catergoryId)
       print('---------->product',products)
    else:
         products = Product.get_all_products()
         print('---------->else product',products)
    data = {}
    data['catergories'] = catergories
    data['products'] = products
    
    print('---------->req',data)
    print(request.session.get('customer_email'))
    return render(request,'chairapp/HomePage.html', data)

# Template Link
@csrf_exempt
def about(request):

    teck_pages(request)
    count_button_video_duration(request)
    return render(request,'chairapp/about.html')
def why(request):
    teck_pages(request)
    return render(request,'chairapp/why.html')
def product(request):
    teck_pages(request)
    if request.method == 'POST':
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
      return redirect('product')
    cart = request.session.get('cart')

    if not cart:
         request.session.cart = {}
         print('---->hjvhhv',cart)
    # end cart check
    products = None
    catergories = Catergory.get_all_categories()
    catergoryId = request.GET.get('catergory')
    print('------>',catergoryId,catergories)
    if catergoryId:
       products = Product.get_all_products_by_catergoryid(catergoryId)
       print('---------->product',products)
    else:
         products = Product.get_all_products()
         print('---------->else product',products)
    data = {}
    data['catergories'] = catergories
    data['products'] = products
    
    print('---------->req',data)
    print(request.session.get('customer_email'))
    return render(request,'chairapp/product.html',data)
   
def testimonial(request):
    teck_pages(request)
    return render(request,'chairapp/testimonial.html')
def forgot(request):
    teck_pages(request)
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
          forgetpass = Register_Customer.objects.get(emailaddress=forgot_password)
          forgetpass.forgot_password_token = token
          print('--->token',token)
          print('-------> forgot',forgot_password)
          forgetpass.save()
          send_forget_password_mail(forgot_password , token)
          error_message = "Email is sent to emailaddress !!"
          return render(request,'chairapp/forgot.html',{'error':error_message})         
    except Exception  as e:
        print(e)
    return render(request,'chairapp/forgot.html')
def createpassword(request,token):
    teck_pages(request)
    context = {}
    try:
         
         if request.method == 'POST':
              new_change_pass = request.POST.get('new_change_password')
              confirm_change_password = request.POST.get('confirm_change_password')
              print(new_change_pass)
              print(confirm_change_password)
              new_change_password = make_password(new_change_pass)
              print('------------->>>>>>',new_change_password)
              CreateNewpassword = Register_Customer.objects.get(forgot_password_token = token)  
              print(CreateNewpassword)  
              CreateNewpassword.password = new_change_password      
              CreateNewpassword.save()
              print('success')            
         
    except Exception as e:
         print(e)
    return render(request,'chairapp/createpassword.html')
def tnc(request):
    teck_pages(request)
    return render(request,'chairapp/tnc.html')
def addtocart(request):
    teck_pages(request)
    print(request.session.get('cart'))
    ids = list(request.session.get('cart').keys())
    print('-------->ids',ids)
    products = Product.get_product_by_id(ids)
    print('----------------------->productids',products)
    customer_email = request.session.get('customer_email')
    customer = Register_Customer.objects.get(emailaddress=customer_email)
    print('--------->first name',customer.first_name)
    context = {
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'address': customer.address,
        'phone': customer.phone,
        'products':products
    }
    return render(request,'chairapp/addtocart.html',context)


def profile(request):
    teck_pages(request)
    customer_email = request.session.get('customer_email')
    print('----->customeremail',customer_email)
    customer_id = request.session.get('customer_id')
    print('---------->id of customer',customer_id)
    customer = Register_Customer.objects.get(emailaddress=customer_email)
    print('------->email gettimng',customer)
    if request.method == 'POST':
        customer.username = request.POST.get('username')
        customer.emailaddress = request.POST.get('emailaddress')
        customer.bio = request.POST.get('bio')
        customer.age = request.POST.get('age')
        customer.address = request.POST.get('address')
        customer.phone = request.POST.get('phone')
        customer.first_name = request.POST.get('first_name')
        customer.middle_name = request.POST.get('middle_name')
        customer.last_name = request.POST.get('last_name')
        if request.FILES.get('image'):
            
            uploaded_image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_image.name, uploaded_image)
            customer.image = fs.url(filename)
        
        customer.save()
        return redirect('profile')
    
    return render(request, 'chairapp/profile.html', {'customer': customer})

def logout(request):
    teck_pages(request)
    request.session.clear()
    return redirect('/login')
def product_detail(request):
    teck_pages(request)
    checkout(request)
    return render(request,'chairapp/product_detail.html')


def product_detail(request,id):
    teck_pages(request)
    product=Product.objects.filter(id=id).first()
 
    reviews = ReviewRating.objects.filter(product=product)
    review_count = reviews.count()
    review_avg = reviews.aggregate(Avg('rating'))['rating__avg']



    context = {'product': product, 'reviews': reviews,'review_count': review_count,
        'review_avg': review_avg }
    
    return render(request,'chairapp/product_detail.html',context)



def submit_review(request,product_id):
   url = request.META.get('HTTP_REFERER')  # get last url
   
   #return HttpResponse(url)
   if request.method == 'POST':  # check post

        form = ReviewForm(request.POST)
        if form.is_valid():
            
            data = ReviewRating()  # create relation with model
            data.subject = form.cleaned_data['subject']
            data.review = form.cleaned_data['review']
            data.rating = form.cleaned_data['rating']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id=product_id
            

            customer_email = request.session['customer_id']

            data.customer = customer_email
            data.save()  # save data to table
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            
            return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)


def edit_review(request, review_id):
    review = ReviewRating.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect('product_detail', id=review.product.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'chairapp/edit_review.html', {'form': form})


def delete_review(request, review_id):
    review = get_object_or_404(ReviewRating, id=review_id, customer=request.session.get('customer_id'))
    product_id = review.product_id
    review.delete()
    return redirect('product_detail', id=product_id)
def checkout(request):
    if request.method == 'POST':
        customer_email = request.session.get('customer_email')
        customer = Register_Customer.objects.get(emailaddress=customer_email)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        customer_address = request.POST.get('address-type')
        customer_address2 = request.POST.get('new-address')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        total_quantity = 0  # initialize total quantity to 0
        for product_id in cart.keys():
            quantity = cart[product_id]
            total_quantity += quantity  # update total quantity
            product = products.filter(id=product_id).first()
            Order = order(customer=customer, product=product, price=product.price, quantity=quantity, phone=phone, customer_address=customer_address, customer_address2=customer_address)
            Order.save()
        del request.session['cart']
        print('-------------->all detail getting', customer_email, first_name, last_name, phone, customer_address, customer_address2, cart, product)
        print('Total Quantity:', total_quantity)
        return HttpResponse('done')

def orders(request):
    teck_pages(request)
    customer = request.session.get('customer_id')
    orderss = order.get_order_by_customer(customer)
    print(orderss)
    return render(request,'chairapp/orders.html',{'order':orderss})
def confirmation(request):
    teck_pages(request)
    customer_email = request.session.get('customer_email')
    customer = Register_Customer.objects.get(emailaddress=customer_email)
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone = request.POST.get('phone')
    context = {'customer_email': customer_email, 'first_name': first_name,'last_name': last_name,
        'phone': phone }
    
    return render(request,'chairapp/confirmation.html',context)
