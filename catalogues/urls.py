from django.urls import path
from . import views

app_name = 'catalogues'
urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('search/', views.search, name='search'),
    path('favourites', views.favourites, name='favourites'),
]
