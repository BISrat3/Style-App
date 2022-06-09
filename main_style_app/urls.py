from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.Shirt.as_view(), name="shirt_home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductsList.as_view(), name= "product_list"),
    path('products/category_id/<int:pk>', views.ProductDetail.as_view(), name= "product_detail"),
    path('products/oxfordshirt', views.OxfordList.as_view(), name= "oxford_shirt"),
    path('products/oxfordshirt/<int:pk>/', views.OxfordDetail.as_view(), name= "oxford_detail"),
    path('products/linenshirt/<int:pk>/', views.LinenDetail.as_view(), name= "linen_detail"),
    path('products/flannelshirt/<int:pk>/', views.FlannelDetail.as_view(), name= "flannel_detail"),
    path('products/classicshirt/<int:pk>/', views.ClassicDetail.as_view(), name= "classic_detail"),
    path('products/denimshirt/<int:pk>/', views.DenimDetail.as_view(), name= "denim_detail"),
    path('products/denimshirt', views.DenimList.as_view(), name= "denim_shirt"),
    path('products/flannelshirt', views.FlannelList.as_view(), name= "flannel_shirt"),
    path('products/linenshirt', views.LinenList.as_view(), name= "linen_shirt"),
    path('products/classicshirt', views.ClassicList.as_view(), name= "classic_shirt"),
    path('products/comment/<int:pk>', views.ReveiwCreate.as_view(), name="create_comment"),
    path('products/comment/<int:pk>/update', views.ReviewUpdate.as_view(), name="comment_update"),
    path('products/comment/<int:pk>/delete', views.ReviewDelete.as_view(), name="comment_delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
]