from django.shortcuts import redirect, render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from .models import BookHave, BookNeed
from categories.models import Category


class BookHaveUpdateView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
    model = BookHave
    template_name = 'books/book_have_update.html'
    login_url = 'account_login'
    fields = [
        'category',
        'name',
        'author',
        'description',
        'image',
    ]

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('home')
    
    
class BookHaveDeleteView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     DeleteView):
    model = BookHave
    template_name = 'books/book_have_delete.html'

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('home')
    

class BookNeedUpdateView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
    model = BookNeed
    template_name = 'books/book_need_update.html'
    login_url = 'account_login'
    fields = [
        'category',
        'name',
        'author',
    ]

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('home')


class BookNeedDeleteView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     DeleteView):
    model = BookNeed
    template_name = 'books/book_need_delete.html'

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('home')
    

def match_results(request):
    if request.user.is_anonymous:
        return redirect('account_login')
    
    context = dict()
    
    user_need_books = BookNeed.objects.filter(user=request.user)
    user_need_books_name = list()
    for book in user_need_books: 
        user_need_books_name.append(book.name)
    users_have_book = BookHave.objects.filter(
            Q(name__in=user_need_books_name) | ~Q(user=request.user)
        )
    context['book_have_list'] = users_have_book
    
    
    user_have_books = BookHave.objects.filter(user=request.user)
    user_have_books_name = list()
    for book in user_have_books: 
        user_have_books_name.append(book.name)
    users_need_book = BookNeed.objects.filter(
            Q(name__in=user_have_books_name) | ~Q(user=request.user)
        )
    context['book_need_list'] = users_need_book
    
    
    users_have_book_name = list()
    for book in users_have_book:
        users_have_book_name.append(book.user)
    
    book_have_match_list = users_need_book.filter(user__in=users_have_book_name)
    
    users_need_book_name = list()
    for book in users_need_book:
        users_need_book_name.append(book.user)
    
    book_need_match_list = users_have_book.filter(user__in=users_need_book_name)
    
    # Book I have (someone need it)
    context['book_have_match_list'] = book_have_match_list
    # Books others have  (I need)
    context['book_need_match_list'] = book_need_match_list
    
    context['book_have_need_match_list'] = zip(book_have_match_list, book_need_match_list)
    
        
        
    return render(request, 'books/book_match_results.html', context)

        