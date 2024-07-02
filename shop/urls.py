from django.urls import path
from shop.views import index, product_details

urlpatterns = [
    path('home/', index, name='home'),
    path('category/<slug:category_slug>/products', index, name='products_of_category'),
    path('product_detail/<slug:slug>', product_details, name='product_detail'),
]
