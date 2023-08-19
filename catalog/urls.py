from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', ProductsListView.as_view(), name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('posts/', BlogPostListView.as_view(), name='posts'),
    path('post/create/', BlogPostCreateView.as_view(), name='post_create'),
    path('post/detail/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('post/delete/<slug:slug>/', BlogPostDeleteView.as_view(), name='post_delete'),
    path('post/update/<slug:slug>/', BlogPostUpdateView.as_view(), name='post_update')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
