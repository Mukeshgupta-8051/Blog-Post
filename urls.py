from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('AddBlog', views.AddBlog, name = 'AddBlog'),
    path('displayBlog', views.displayBlog, name = 'displayBlog'),
    path('searchBlog', views.searchBlog, name = 'searchBlog'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('updateBlog/<int:id>', views.updateBlog, name = 'updateBlog'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]