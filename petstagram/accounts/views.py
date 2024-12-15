from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.accounts.forms import AppUserCreationForm

UserModel = get_user_model()


# def login(request):
#     return render(request, "accounts/login-page.html")


class AppUserLoginView(LoginView):
    template_name = "accounts/login-page.html"


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response


# def register(request):
#     return render(request, "accounts/register-page.html")


def profile_delete(request, pk):
    return render(request, "accounts/profile-delete-page.html")


def profile_details(request, pk):
    return render(request, "accounts/profile-details-page.html")


def profile_edit(request, pk):
    return render(request, "accounts/profile-edit-page.html")
