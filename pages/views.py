from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BookHaveCreateForm

# Create your views here.


def home(request):
    context = dict()
    if request.method == 'POST' and 'bookhave' in request.POST:
        form = BookHaveCreateForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()

        form = BookHaveCreateForm()
        context['form'] = form
        
    else:
        form = BookHaveCreateForm()
        context['form'] = form
    return render(request, 'home.html', context)


class AboutPageView(TemplateView):
    template_name = 'about.html'
