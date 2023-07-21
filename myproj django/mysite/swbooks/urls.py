from django.urls import path
from . import views
urlpatterns=[
    path('', views.show_books , name='show_books'),
    path('add_book/', views.Add_book , name='Add_book'),
]