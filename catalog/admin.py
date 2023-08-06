from django.contrib import admin

from catalog.models import Product, Category, BlogPost


# Register your models here.
@admin.register(Product)
class Products(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Category)
class Catalog(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ('pk', 'title',)
