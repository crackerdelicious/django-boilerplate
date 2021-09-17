from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpRequest
from django.conf import settings
from django.urls import reverse_lazy

from apps.accounts.forms import AccountsLoginForm


class AccountsLoginView(LoginView):
    template_name = 'accounts/base.html'
    form_class = AccountsLoginForm


class AccountsLogoutView(LoginView):
    template_name = 'accounts/base.html'


class AccountsProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/base.html'
    login_url = settings.LOGIN_URL

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.template_name)
