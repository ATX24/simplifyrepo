from django.urls import path
from . import views

app_name = 'simplify'
urlpatterns = [
    path('', views.index, name='index'),
    path('ans', views.ans, name='ans'),
    path('about', views.about, name='about')
    
]