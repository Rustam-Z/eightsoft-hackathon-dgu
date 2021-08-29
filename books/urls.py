from django.urls import path
from .views import (
    BookHaveUpdateView,
    BookHaveDeleteView,
    BookNeedUpdateView,
    BookNeedDeleteView,
    match_results,
)
from . import views

urlpatterns = [
    path('have/<uuid:pk>/update',
         BookHaveUpdateView.as_view(),
         name='book_have_update'),

    path('have/<uuid:pk>/delete',
         BookHaveDeleteView.as_view(),
         name='book_have_delete'),

    path('need/<uuid:pk>/update',
         BookNeedUpdateView.as_view(),
         name='book_need_update'),

    path('need/<uuid:pk>/delete',
         BookNeedDeleteView.as_view(),
         name='book_need_delete'),

    path('match/',
         views.match_results,
         name='book_match_list'),
    
    path('book_search/',
         views.book_search,
         name='book_search'),
    
    path('book_search_library/',
         views.book_search_library,
         name='book_search_library'),
]