from django.conf import settings
from django.urls import path
from chairapp import views
from chairapp.view import register,login
from django.conf import settings
from django.conf.urls.static import static
from .views import Home,product
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
    path('addtocart',views.addtocart,name='addtocart'),
    path('profile/', views.profile, name='profile'),
    path('logout',views.logout,name='logout'),
    path('products/<str:id>',views.product_detail,name='product_detail'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('checkout', views.checkout, name='checkout'),
    path('orders', views.orders, name='orders'),
    path('confirmation', views.confirmation, name='confirmation'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
