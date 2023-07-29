from django.shortcuts import render

from catalog.models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'title': 'Главная',
        'objict_list': products
    }
    return render(request, 'catalog/catalog.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        'title': 'Контакты',
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)
