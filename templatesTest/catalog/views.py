from django.shortcuts import render
from .models import Product

menu = {"Главная":"/", "Каталог":"/catalog", "О сайте":"/about"}


def catalog_page(request):
    products = Product.objects.all()
    title = "Каталог"
    data = {"title": title, "menu": menu, "products": products}
    return render(request, "./catalog.html", context=data)