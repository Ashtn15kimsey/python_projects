from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products = ["apple", "cherries", "pineapples", "strawberries"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)