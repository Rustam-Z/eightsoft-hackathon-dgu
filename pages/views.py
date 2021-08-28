from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.decorators.http import require_GET, require_POST

from .forms import BookHaveCreateForm, BookNeedCreateForm
from categories.models import Category
from books.models import BookHave, BookNeed

# Create your views here.


def home(request):
    context = dict()
    categories = Category.objects.all()
    form_have = BookHaveCreateForm()
    form_need = BookNeedCreateForm()
    if request.user.is_authenticated:
        books_have_list = BookHave.objects.filter(user=request.user)
        context['book_have_list'] = books_have_list
        books_need_list = BookNeed.objects.filter(user=request.user)
        context['book_need_list'] = books_need_list
    context['form_have'] = form_have
    context['form_need'] = form_need
    context['categories'] = categories
        
    return render(request, 'home.html', context)


@require_POST
def book_new(request):
    if request.user.is_anonymous:
        return redirect('account_login')
    
    if request.method == 'POST' and 'book_have' in request.POST:
        form = BookHaveCreateForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        
    if request.method == 'POST' and 'book_need' in request.POST:
        form = BookNeedCreateForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        
    return redirect('home')


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactsPageView(TemplateView):
    template_name = 'pages/contacts.html'


class MatchPageView(TemplateView):
    template_name = 'pages/match.html'   


class LibraryPageView(TemplateView):
    template_name = 'pages/library.html' 