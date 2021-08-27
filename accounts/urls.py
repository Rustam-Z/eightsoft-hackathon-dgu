from django.urls import path
from .views import (
     SignupPageView,
     AccountUpdateView,
)

urlpatterns = [
     path('signup/', SignupPageView.as_view(), name='signup'),
     
     path('<slug:slug>/update',
          AccountUpdateView.as_view(),
          name='account_update'),
]