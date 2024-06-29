from django.shortcuts import render


def product_home(request):
    return render(request, 'shop/home.html')


def product_details(request):
    return render(request, 'shop/detail.html')