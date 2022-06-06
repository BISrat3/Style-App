from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import ShirtHome


class About(TemplateView):
    template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse("Product About")

# class Shirt_Home:
#     def __init__(self, name, image, price):
#         self.name = name
#         self.image = image
#         self.price = price


class Shirt(TemplateView):
    template_name ="shirt_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shirts"] = ShirtHome
        return context