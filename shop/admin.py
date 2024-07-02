from django.contrib import admin
from shop.models import Category, Product, Order, Comment


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
