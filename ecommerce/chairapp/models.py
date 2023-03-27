from django.db import models
from .catergory import Catergory
# Create your models here.
from distutils.command.upload import upload
from email.policy import default
from unicodedata import category, name
from django.contrib.auth.models import User,auth

# product models
class Product(models.Model):
    name = models.CharField(max_length=50) 
    price = models.IntegerField(default=0)
    PrevPrice = models.IntegerField(default=0)
    catergory = models.ForeignKey(Catergory,on_delete=models.CASCADE,default = 1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='upload/product/')
  

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
class NewPassCreate(models.Model):
   emailaddress = models.OneToOneField(Register_Customer,on_delete=models.CASCADE)  
   forgot_password_token = models.CharField(max_length=100,null=True) 
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.forgot_password_token
  
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
  





