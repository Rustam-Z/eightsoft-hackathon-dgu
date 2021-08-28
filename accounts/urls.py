from django.urls import path
from .views import (
     SignupPageView,
     AccountUpdateView,
     AccountDetailView,
)

urlpatterns = [
     path('signup/', SignupPageView.as_view(), name='signup'),
     
     path('<slug:slug>/update',
          AccountUpdateView.as_view(),
          name='account_update'),
     
     path('<slug:slug>/detail',
          AccountDetailView.as_view(),
          name='account_detail'),
]