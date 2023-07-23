from django.urls import path
from catalog.views import index, contacts

urlpatterns = [
    path('', index, name='catalog'),
    path('contacts/', contacts, name='contacts')
]