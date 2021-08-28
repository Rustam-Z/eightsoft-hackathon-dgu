from django.urls import path
from .views import AboutPageView, ContactsPageView, LibraryPageView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_new', views.book_new, name='book_new'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('library/', LibraryPageView.as_view(), name='library'),
]