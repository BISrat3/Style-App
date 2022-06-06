from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import ShirtHome
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
class ProductList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["shirts"] = ShirtHome.objects.filter(
                name__icontains=name, user=self.request.user)
        else:
            context["shirts"] = ShirtHome.objects.all()
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
