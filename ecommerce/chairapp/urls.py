from django.urls import path
from chairapp import views

urlpatterns = [
    path('',views.index,name='index'),
]