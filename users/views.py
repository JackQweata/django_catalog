from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic.edit import CreateView

from config import settings
from .forms import UserRegisterForm, PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site

from .models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        token_reg = default_token_generator.make_token(user)
        user.is_active = False
        user.token_reg = token_reg
        user.save()

        current_site = get_current_site(self.request)
        verify_url = reverse('users:verify', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                                     'token': token_reg})

        verify_link = f'http://{current_site.domain}{verify_url}'
        mail_subject = 'Подтверждение регистрации'

        send_mail(mail_subject, verify_link, settings.EMAIL_HOST_USER, [user.email])

        return super().form_valid(form)


def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and user.token_reg == token:
        user.is_active = True
        user.token_reg = ''
        user.save()
        return render(request, 'users/verification.html', {'is_valid': True})
    else:
        return render(request, 'users/verification.html', {'is_valid': False})


def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if user:
                new_password = User.objects.make_random_password()
                user.set_password(new_password)
                user.save()

                mail_subject = 'Восстановление пароля'
                message = f'Ваш новый пароль: {new_password}'
                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])

                return HttpResponse('Письмо с новым паролем отправлено на вашу почту.')
            else:
                return HttpResponse('Пользователь с такой почтой не найден.')
    else:
        form = PasswordResetForm()
    return render(request, "users/password_reset.html", {"form": form})
