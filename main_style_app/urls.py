from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.Shirt.as_view(), name="shirt_home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductsList.as_view(), name= "product_list"),
    path('products/<int:pk>/categories/', views.CategoryList.as_view(), name= "categories_list"),
    path('products/oxfordshirt', views.OxfordList.as_view(), name= "oxford_shirt"),
    path('products/denimshirt', views.DenimList.as_view(), name= "denim_shirt"),
    path('products/flannelshirt', views.FlannelList.as_view(), name= "flannel_shirt"),
    path('products/linenshirt', views.LinenList.as_view(), name= "linen_shirt"),
    path('products/classicshirt', views.ClassicList.as_view(), name= "classic_shirt"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
]