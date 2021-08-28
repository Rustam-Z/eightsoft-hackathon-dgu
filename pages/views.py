from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BookHaveCreateForm, BookNeedCreateForm

# Create your views here.


def home(request):
    context = dict()
    if request.method == 'POST' and 'book_have' in request.POST:
        form = BookHaveCreateForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        form_have = BookHaveCreateForm()
        form_need = BookNeedCreateForm()
        context['form_have'] = form_have
        context['form_need'] = form_need
        
    if request.method == 'POST' and 'book_need' in request.POST:
        form = BookNeedCreateForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        form_have = BookHaveCreateForm()
        form_need = BookNeedCreateForm()
        context['form_have'] = form_have
        context['form_need'] = form_need
        
    else:
        form_have = BookHaveCreateForm()
        form_need = BookNeedCreateForm()
        context['form_have'] = form_have
        context['form_need'] = form_need
        
    return render(request, 'home.html', context)


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class MatchPageView(TemplateView):
    template_name = 'match.html'   


class LibraryPageView(TemplateView):
    template_name = 'library.html' 