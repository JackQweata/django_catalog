from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', index, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:product_id>', product_detail, name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
