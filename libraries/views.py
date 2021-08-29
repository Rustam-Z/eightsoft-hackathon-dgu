from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q

from .models import Book, Library
from .forms import LibraryRegionForm
from categories.models import Category

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
    if request.user.is_authenticated:
        if request.method == 'POST':
            context = dict()
            form = LibraryRegionForm()
            libraries_by_region = Library.objects.filter(region=request.POST['region'])
            context['libraries'] = libraries_by_region
            context['form'] = form
            context['region_name'] = request.POST['region']
            return render(request, 'libraries/library.html', context)
        
        return redirect('library')
    return redirect('home')


class LibraryDetailView(LoginRequiredMixin,
                        DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'libraries/library_book_list.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def library_books_by_category(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            context = dict()
            print(request.POST['category'])
            library_books_by_category = Book.objects.filter(
                Q(category=request.POST['category']) & Q(library=request.POST['library'])
            )
            context['library_books_by_category'] = library_books_by_category
            context['library'] = Book.objects.filter(library=request.POST['library']).first().library
            context['category_name'] = library_books_by_category.first().category.name
            context['categories'] = Category.objects.all()
            return render(request, 'libraries/library_book_category_list.html', context)
        
        return reverse_lazy('library_detail')
    return redirect('home')