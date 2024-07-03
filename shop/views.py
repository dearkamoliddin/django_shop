from django.shortcuts import render, redirect
from shop.models import Product, Category, Comment, Order
from shop.forms import CommentModelForm, OrderModelForm


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
    related_product = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    comment_list = Comment.objects.filter(product__slug=slug)[:3]
    commentForm = CommentModelForm()
    orderForm = OrderModelForm()
    new_comment = None
    new_order = None
    if request.method == 'POST':
        commentForm = CommentModelForm(data=request.POST)
        orderForm = OrderModelForm(data=request.POST)
        if commentForm.is_valid():
            new_comment = commentForm.save(commit=False)
            new_comment.product = product
            new_comment.save()
        elif orderForm.is_valid():
            new_order = orderForm.save(commit=False)
            new_order.product = product
            new_order.save()

    context = {
        'product': product,
        'related_product': related_product,
        'commentForm': commentForm,
        'comment_list': comment_list,
        'orderForm': orderForm,
        'new_comment': new_comment,
        'new_order': new_order

    }
    return render(request, 'shop/detail.html', context)

