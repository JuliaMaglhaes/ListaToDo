from django.contrib import admin
from django.urls import path
from ToDo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('listaf/<str:pk>/', listaf, name='listaf'),
    path('deletar/<int:pk>/', deletar, name='deletar'),
]
