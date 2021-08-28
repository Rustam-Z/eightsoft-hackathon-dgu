from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Book, Library
from .forms import LibraryRegionForm

# Create your views here.

def library(request):
    if request.user.is_authenticated:
        context = dict()
        libraries = Library.objects.all()
        context['libraries'] = libraries
        form = LibraryRegionForm()
        context['form'] = form
        return render(request, 'libraries/library.html', context)
    
    return redirect('account_login')


def library_region(request):
    if request.method == 'POST':
        context = dict()
        form = LibraryRegionForm()
        libraries_by_region = Library.objects.filter(region=request.POST['region'])
        context['libraries'] = libraries_by_region
        context['form'] = form
        context['region_name'] = request.POST['region']
        return render(request, 'libraries/library.html', context)
    
    return redirect('library')


class LibraryDetailView(LoginRequiredMixin,
                        DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'libraries/library_book_list.html'
    login_url = 'account_login'