from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.Shirt.as_view(), name="shirt_home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductList.as_view(), name= "product_list"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
]