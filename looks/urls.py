from django.urls import path
from . import views

app_name='looks'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('favourite/<int:pk>/', views.favourite, name='favourite'),
    path('look/<int:pk>/', views.recipe, name='look'),
]
