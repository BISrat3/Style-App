from django.urls import path 
from . import views

urlpatterns =[
    path('', views.ShirtHome.as_view(), name="shirt_home"),
    path('about/', views.About.as_view(), name="about"),
    # path('shirts/', views.ShirtList.as_view)
]