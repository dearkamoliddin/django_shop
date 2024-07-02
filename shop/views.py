from django.shortcuts import render
from shop.models import Product, Category


def index(request, category_slug=None):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    home = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        'products': products,
        'categories': categories,
        'home': home,
    }
    return render(request, 'shop/home.html', context)


def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/detail.html', context)






