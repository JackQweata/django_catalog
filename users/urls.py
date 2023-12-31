from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
  path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('refister/', RegisterView.as_view(), name='register'),
  path('verify/<str:uidb64>/<str:token>/', verify_email, name='verify'),
  path('password_reset/', password_reset, name='password_reset'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
