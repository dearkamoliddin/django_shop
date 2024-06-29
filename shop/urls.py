from django.urls import path
from shop.views import product_home, product_details

urlpatterns = [
    path('home/', product_home, name='product_home'),
    path('detail/', product_details, name='product_details'),
]
