from itertools import product
from sre_constants import SUCCESS
from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Products, ShirtHome, Category, Review, User, StoreSlide
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.urls import reverse
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class About(TemplateView):
    template_name = "about.html"

class Store(TemplateView):
    template_name ="mens_cloth_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shirts"] = ShirtHome.objects.all()
        return context

def StoreSlide(request):
    
    slides = StoreSlide.objects.all()
    context = {
            'slides': slides
        }
    return render(request, 'mens_cloth_home.html', context)

@method_decorator(login_required, name='dispatch')
class ProductsList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        
        if name != None:
            context["shirts"] = Products.objects.filter(
                name__icontains=name)
        else:
            context["shirts"] = Products.objects.all()
        return context


class CategoryList(TemplateView):
    template_name = "categories_list.html"

@method_decorator(login_required, name='dispatch')
class ShirtList(TemplateView):
    template_name = "shirt_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 5, 
            )
        return context

@method_decorator(login_required, name='dispatch')
class PantList(TemplateView):
    template_name = "pants_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["pants"] = Products.objects.filter( category_id= 1, 
            )
        return context

class PantDetail(DetailView):
    model = Products
    template_name = "pants_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id = self.request.GET.get("id")
        context['reviews'] = Review.objects.filter(product=self.object)
        context["pants"] = Products.objects.get(id__contains= context['products'].id )
        return context

@method_decorator(login_required, name='dispatch')      
class ShortsList(TemplateView):
    template_name = "shorts_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 3, 
            )
        return context

@method_decorator(login_required, name='dispatch')
class ShoesList(TemplateView):
    template_name = "shoes_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["Shoes"] = Products.objects.filter(category_id= 2, 
            )
        return context


@method_decorator(login_required, name='dispatch')
class WatchesList(TemplateView):
    template_name = "watches_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 4, 
            )
        return context

class ProductDetail(DetailView):
    model = Products
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # name = self.request.GET.get(" name")
        context['reviews'] = Review.objects.filter(product=self.object)
        context["shirts"] = Products.objects.get(id__contains= context['products'].id)
        return context

class ShirtDetail(DetailView):
    model = Products
    template_name = "shirt_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        context["shirts"] = Products.objects.get(id__contains= context['products'].id )
        return context


class WatchesDetail(DetailView):
    model = Products
    template_name = "watches_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id = self.request.GET.get("id")
        context['reviews'] = Review.objects.filter(product=self.object)
        context["shirts"] = Products.objects.get(id__contains= context['products'].id )
        return context

class ShoesDetail(DetailView):
    model = Products
    template_name = "shoes_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id = self.request.GET.get("id")
        context['reviews'] = Review.objects.filter(product=self.object)
        context["Shoes"] = Products.objects.get(id__contains= context['products'].id )
        return context

class ShortsDetail(DetailView):
    model = Products
    template_name = "shorts_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id = self.request.GET.get("id")
        context['reviews'] = Review.objects.filter(product=self.object)
        context["shirts"] = Products.objects.get(id__contains= context['products'].id )
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
            return redirect("product_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


@method_decorator(login_required, name='dispatch')
class ReveiwCreate(View):
    def post(self, request, pk, user_id):
        print(user_id)
        comment= request.POST.get('comment')
        product = Products.objects.get(pk = pk)
        reviewerUser= User.objects.get(id= user_id)
        print(reviewerUser)
        Review.objects.create(comment=comment, product = product, Reviewers=reviewerUser)
        return redirect('shirt_detail', pk=pk)
        
class ReviewUpdate(UpdateView):
    model = Review
    fields = ['comment']
    template_name = "comment_update.html"
    success_url = '/products'

class ReviewDelete(DeleteView):
    model = Review
    template_name = "comment_delete.html"
    success_url = "/products/"

    