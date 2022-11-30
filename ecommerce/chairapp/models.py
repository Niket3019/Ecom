from django.db import models
from .catergory import Catergory
# Create your models here.
from distutils.command.upload import upload
from email.policy import default
from unicodedata import category, name
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