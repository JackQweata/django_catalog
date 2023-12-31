from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product/create/', login_required(ProductCreateView.as_view()), name='product_create'),
    path('product/update/<int:pk>', login_required(ProductUpdateView.as_view()), name='product_update'),
    path('product/delete/<int:pk>', login_required(ProductDeleteView.as_view()), name='product_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
