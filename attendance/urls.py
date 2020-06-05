from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='attendance-home'),
    path('about/', views.about, name='attendance-about'),
]
