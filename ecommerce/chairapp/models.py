from django.db import models
from .catergory import Catergory
# Create your models here.
from distutils.command.upload import upload
from email.policy import default
from unicodedata import category, name
from django.contrib.auth.models import User,auth
import datetime
# product models
class Product(models.Model):
    name = models.CharField(max_length=50) 
    price = models.IntegerField(default=0)
    PrevPrice = models.IntegerField(default=0)
    catergory = models.ForeignKey(Catergory,on_delete=models.CASCADE,default = 1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='upload/product/')
    image1 = models.ImageField(upload_to='upload/product/', null=True, blank=True)
    image2 = models.ImageField(upload_to='upload/product/', null=True, blank=True)
    image3 = models.ImageField(upload_to='upload/product/', null=True, blank=True)
  
    
    @staticmethod
    def get_product_by_id(ids):
       return Product.objects.filter(id__in=ids)
    @staticmethod 
    def get_all_products():
      return Product.objects.all() 

    @staticmethod 
    def get_all_products_by_catergoryid(catergory_id):
      if catergory_id:
       return Product.objects.filter(catergory = catergory_id) 
      else :
        return Product.get_all_products()
  
# register models
class Register_Customer(models.Model):
    username = models.CharField(max_length=20)
    fullname = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=40)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=250)
    confirmpassword = models.CharField(max_length=250)
    forgot_password_token = models.CharField(max_length=100,null=True) 
    new_change_password = models.CharField(max_length=250,null=True)
    confirm_change_password = models.CharField(max_length=250,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    middle_name = models.CharField(max_length=30, default="", blank=True)
    address = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', default='default.png', blank=True)

    def __str__(self):
      return self.emailaddress
    def EmailisExist(self):
      if Register_Customer.objects.filter(emailaddress = self.emailaddress):
        return True
      return False
    def PhoneisExist(self):
      if Register_Customer.objects.filter(phone = self.phone):
        return True
      return False
    def UsernameisExist(self):
      if Register_Customer.objects.filter(username = self.username):
        return True
      return False
    @staticmethod
    def get_customer_by_email(emailaddress):
     try:
      return Register_Customer.objects.get(emailaddress=emailaddress)
     except:
       return False

  
class Track_User_Path(models.Model):
    ip_address = models.GenericIPAddressField()
    url = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    date_time = models.CharField(max_length=255)
    def __str__(self):
        return self.ip_address
class count_button_click(models.Model):
    ip_address = models.CharField(max_length=255,null=True)
    tag_name = models.CharField(max_length=255,null=True)
    click_count = models.CharField(max_length=255,null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name  
class VedioDuration(models.Model):
    ip_address = models.CharField(max_length=255,null=True)
    start_time = models.CharField(max_length=255,null=True)
    pause_time = models.CharField(max_length=255,null=True)
    duration = models.CharField(max_length=255,null=True)
    total_duration = models.CharField(max_length=255,null=True)
    date_time = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.total_duration  
    


      
class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.subject
class order(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   customer = models.ForeignKey(Register_Customer,on_delete=models.CASCADE)
   customer_address = models.CharField(max_length=100, blank=True)
   customer_address2 = models.CharField(max_length=100, blank=True)
   phone = models.CharField(max_length=15, default='')
   quantity = models.IntegerField(default=1)
   price = models.IntegerField()
   date = models.DateField(default=datetime.datetime.today)
   status = models.BooleanField(default=False)
   def placeorder(self):
      self.save()
   @staticmethod
   def get_order_by_customer(customer_email):
      return order\
        .objects\
          .filter(customer=customer_email).order_by('-date')




