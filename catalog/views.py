from django.shortcuts import render


def index(request):
    return render(request, 'catalog/catalog.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')
