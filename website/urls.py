from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news_letter', views.news_letter, name='newsletter'),
]
