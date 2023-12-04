from django.shortcuts import render

menu = {"Главная":"/", "Каталог":"/catalog", "О сайте":"/about"}


def main_page(request):
	title = "Главная"
	data = {"title": title, "menu": menu}
	return render(request, "./index.html", context=data)


def about_page(request):
	title = "О компании"
	data = {"title": title, "menu": menu}
	return render(request, "./about.html", context=data)