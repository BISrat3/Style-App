from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView



class About(TemplateView):
    template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse("Product About")

class Shirt_Home:
    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price


shirts = [
  Shirt_Home("New Design", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8sqMlFSykcvvgoDi0wc_JXzIJX2Jb5cFy5QyMVowwXkoWPfhMKzArWXJquTm0Azn5fd4&usqp=CAU",
          "$35"),
  Shirt_Home("Fannel!",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSvON2DQFdxB8lTJMPdpIPeB52fnHa65RQxg&usqp=CAU", "$50"),
  Shirt_Home("Wrinkle-Free", "https://cdn.shopify.com/s/files/1/0129/1072/products/PARRINO-UNTUCKIT-PERFORMANCE-POLYGIENE-CHECK-BLUE-2_1600x.jpg?v=1588802117", "$55"),

  Shirt_Home("Versace",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0xxwDuJTwlhvJLuIC4exgm166s4swzKC3Vw&usqp=CAU", "$75"),
          
]

class ShirtHome(TemplateView):
    template_name ="shirt_home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shirts"] = shirts 
        return context