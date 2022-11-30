from django.conf import settings
from django.urls import path
from chairapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.HomePage,name='HomePage'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('why',views.why,name='why'),
    path('product',views.product,name='product'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('forgot',views.forgot,name='forgot'),
    path('tnc',views.tnc,name='tnc'),
    path('register',views.register,name='register'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
