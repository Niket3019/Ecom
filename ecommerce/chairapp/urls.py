from django.conf import settings
from django.urls import path
from chairapp import views
from chairapp.view import register,login
from django.conf import settings
from django.conf.urls.static import static
from .views import Home
urlpatterns = [
    path('',Home.as_view(),name='HomePage'),
    path('about',views.about,name='about'),
    path('login',login.Login.as_view(),name='login'),
    path('why',views.why,name='why'),
    path('product',views.product,name='product'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('forgot',views.forgot,name='forgot'),
    path('createpassword/<token>/',views.createpassword,name='createpassword'),
    path('tnc',views.tnc,name='tnc'),
    path('register',register.register.as_view(),name='register'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
