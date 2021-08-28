from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('', views.library, name='library'),
    path('region/', views.library_region, name='library_region'),
    
         path('<slug:slug>/detail',
          LibraryDetailView.as_view(),
          name='library_detail'),
]