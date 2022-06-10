from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.Shirt.as_view(), name="shirt_home"),
    path('about/', views.About.as_view(), name="about"),
    path('products/', views.ProductsList.as_view(), name= "product_list"),
    path('products/category_id/<int:pk>', views.ProductDetail.as_view(), name= "product_detail"),
    path('products/shirts', views.ShirtList.as_view(), name= "shirt_list"),
    path('products/shirts/<int:pk>/', views.ShirtDetail.as_view(), name= "shirt_detail"),
    path('products/pants/<int:pk>/', views.PantDetail.as_view(), name= "pants_detail"),
    path('products/flannelshirt/<int:pk>/', views.FlannelDetail.as_view(), name= "flannel_detail"),
    path('products/classicshirt/<int:pk>/', views.ClassicDetail.as_view(), name= "classic_detail"),
    path('products/denimshirt/<int:pk>/', views.DenimDetail.as_view(), name= "denim_detail"),
    path('products/denimshirt', views.DenimList.as_view(), name= "denim_shirt"),
    path('products/flannelshirt', views.FlannelList.as_view(), name= "flannel_shirt"),
    path('products/pants', views.PantList.as_view(), name= "pants_list"),
    path('products/classicshirt', views.ClassicList.as_view(), name= "classic_shirt"),
    path('products/comment/<int:pk>/<int:user_id>/', views.ReveiwCreate.as_view(), name="create_comment"),
    path('products/comment/<int:pk>/update', views.ReviewUpdate.as_view(), name="comment_update"),
    path('products/comment/<int:pk>/delete', views.ReviewDelete.as_view(), name="comment_delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
]