from django.urls import path
from .views import AboutPageView, ContactsPageView, MatchPageView, LibraryPageView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', AboutPageView.as_view(), name='about'), 
    path('contacts/', ContactsPageView.as_view(), name='contacts'), 
    path('match/', MatchPageView.as_view(), name='match'), 
    path('library/', LibraryPageView.as_view(), name='library'), 

]