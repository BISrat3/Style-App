from unicodedata import category
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Products, ShirtHome, Category
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
        context["shirts"] = ShirtHome.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ProductsList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        
        if name != None:
            context["shirts"] = Products.objects.filter(
                name__icontains=name, user=self.request.user)
        else:
            context["shirts"] = Products.objects.all()
        return context


class CategoryList(TemplateView):
    template_name = "categories_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     name = self.request.GET.get("name")
        
    #     if name != None:
    #         context["shirts"] = Category.filter(
    #             name__icontains=name, user=self.request.user)
    #     else:
    #         context["shirts"] = Category.objects.all()
    #     return context


class OxfordList(TemplateView):
    template_name = "oxford_shirt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 5, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context

class ClassicList(TemplateView):
    template_name = "classic_shirt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 3, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context


class DenimList(TemplateView):
    template_name = "classic_shirt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 3, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context


class LinenList(TemplateView):
    template_name = "linen_shirt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 1, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context

class FlannelList(TemplateView):
    template_name = "flannel_shirt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 4, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
