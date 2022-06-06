from django.urls import path 
from . import views

urlpatterns =[
    path('', views.Shirt.as_view(), name="shirt_home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductList.as_view(), name= "product_list"),
]