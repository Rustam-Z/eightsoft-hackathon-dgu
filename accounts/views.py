from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView

from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'


class AccountUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        UpdateView):
    model = CustomUser
    template_name = 'profile/profile_update.html'
    login_url = 'account_login'
    fields = (
        'email',
        'phone',
        'image',
        'telegram',
        'region',
    )

    def test_func(self):
        obj = self.get_object()
        return obj.slug == self.request.user.slug
    
    def get_success_url(self):
        return reverse_lazy('home')

    # def get_success_url(self):
    #     return reverse_lazy('account_detail',
    #                         kwargs={'slug': self.request.user.slug})
    

class AccountDetailView(LoginRequiredMixin,
                        DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'account/profile_view.html'
    login_url = 'account_login'