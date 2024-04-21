from django.shortcuts import render
from django.views import View
from .models import Product, ProdoctComents, Card


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        contexs = {
            'products':products
        }
        return render(request, "shop.html", contexs)

    def post(self, request):
        seachr = request.POST.get("search")
        products = Product.objects.filter(name__icontains=seachr)
        contexs = {
            'products': products
        }
        return render(request, "shop.html", contexs)


class ShopdetailViews(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        contexs = {
            'product': product
        }
        return render(request, "shop-detail.html", contexs)

class CardView(View):
    def get(self, request):
        products = Product.objects.all()
        contexs = {
            'products':products
        }
        return render(request, "shop.html", contexs)