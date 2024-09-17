import secrets
import random
import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy,reverse
from users.forms import UserRegisterForm, UserProfileForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Потверждение почты",
            message=f"Передите по ссылке для потверждения {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

@login_required
def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))

@login_required
def recovery_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not User.objects.filter(email=email).exists():
            return render(request, template_name='users/recovery_password.html')

        else:
            user = get_object_or_404(User, email=email)
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(new_password)
            user.save()
            send_mail(
                subject="Востановление пароля",
                message=f"Новый пароль {new_password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]

            )
            return redirect(reverse("users:login"))

    return render(request, template_name='users/recovery_password.html')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user