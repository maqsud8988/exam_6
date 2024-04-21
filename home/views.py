# from django.shortcuts import render
# from django.views import View
# from shop.models import Product

from django.shortcuts import render, redirect
from django.views import View
from shop.models import Product
from django.contrib.auth import authenticate

class LandingView(View):
    def get(self, request):
        if not authenticate(request):
            return redirect('login')
        product = Product.objects.all()
        context = {
            "products": product
        }
        return render(request, "index.html", context)


class LandingView(View):
    def get(self, request):
        product = Product.objects.all()
        context = {
            "products": product
        }
        return render(request, "index.html", context)


