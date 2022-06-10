from itertools import product
from sre_constants import SUCCESS
from unicodedata import category
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Products, ShirtHome, Category, Review, User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.urls import reverse
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# from rest_framework import generics

class About(TemplateView):
    # selected=Products.objects.filter(is_featured=True).order_by('category_id')
    template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse("Product About")

# class Shirt_Home:
#     def __init__(self, name, image, price):
#         self.name = name
#         self.image = image
#         self.price = price


class Store(TemplateView):
    template_name ="mens_cloth_home.html"

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
                name__icontains=name)
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


class ShirtList(TemplateView):
    template_name = "shirt_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 5, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context

class PantList(TemplateView):
    template_name = "pants_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["pants"] = Products.objects.filter( category_id= 1, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
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

        
class ShortsList(TemplateView):
    template_name = "shorts_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 3, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context


class ShoesList(TemplateView):
    template_name = "shoes_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter(category_id= 2, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
        return context



class WatchesList(TemplateView):
    template_name = "watches_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter( category_id= 4, 
            )
        # else:
        #     context["shirts"] = Products.objects.all()
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
        context["shirts"] = Products.objects.get(id__contains= context['products'].id )
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


# def filter_price(request):
#     minimumPrice = request.GET['minimumPrice']
#     maximumPrice = request.GET['maximumPrice']
#     allProducts = Products.objects.all().order_by('price').distinct()
#     allProducts = allProducts.filter(products__price__=minimumPrice)
#     allProducts = allProducts.filter(products__price__=maximumPrice)


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
        # prod = Review.objects.get(pk = pk)
        # print(prod.cat_id)
        # if Category.cat_id == 5:  
            # success_url = f'products/oxfordshirt/{prod.cat_id}/'
            # return redirect (f'products/oxfordshirt/{prod.cat_id}/')
        
@method_decorator(login_required, name='dispatch')
class ReviewUpdate(UpdateView):
    model = Review
    fields = ['comment']
    template_name = "comment_update.html"
    def get_success_url(self):
        return reverse('oxford_shirt')

class ReviewDelete(DeleteView):
    model = Review
    template_name = "comment_delete.html"
    success_url = "/products/"

    
        # return redirect (f'products/oxfordshirt/{prod.cat_id}/' )
#     data = render_to_string('product_list.html', {'selected': allProducts})
#     return JsonResponse({'selected': data})

# def filter_price(request):
#     product_filter = RangeFilter(request.GET)
#     return render(request, 'product_list.html',{'product_filter': product_filter})


# class ProductFilter(filters.FilterSet):
#     min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

#     class Meta:
#         model = Products
#         fields = ['min_price', 'max_price']


# class ProductList(generics.ListAPIView):
#     queryset = Products.objects.all()
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = ProductFilter