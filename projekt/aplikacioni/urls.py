from django.urls import path 
from . import views
urlpatterns = [
    path('', views.aplikacioni, name='aplikacioni'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='aboutus')
    
]