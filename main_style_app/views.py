from unicodedata import category
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse 
from django.views.generic.base import TemplateView

from .models import Products, ShirtHome, Category, Review
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.views.generic import DetailView
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django_filters import rest_framework as filters

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
    template_name = "denim_shirt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        context["shirts"] = Products.objects.filter(category_id= 2, 
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

class ProductDetail(DetailView):
    model = Products
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # name = self.request.GET.get("name")
        context["shirts"] = Products.objects.get(id__contains= context['products'].id)
        return context

class OxfordDetail(DetailView):
    model = Products
    template_name = "oxford_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id = self.request.GET.get("id")
        context["shirts"] = Products.objects.get(id__contains= context['products'].id )
        return context

class LinenDetail(DetailView):
    model = Products
    template_name = "linen_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id = self.request.GET.get("id")
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
            return redirect("products_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


def filter_price(request):
    minimumPrice = request.GET['minimumPrice']
    maximumPrice = request.GET['maximumPrice']
    allProducts = Products.objects.all().order_by('price').distinct()
    allProducts = allProducts.filter(products__price__=minimumPrice)
    allProducts = allProducts.filter(products__price__=maximumPrice)


class ReveiwCreate(View):
    def post(self, request, pk):
        comment= request.POST.get('content')
        shirt = Products.objects.get(pk = pk)
        Review.objects.create(comment = comment, shirt = shirt)
        return redirect('product_detail.html')


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