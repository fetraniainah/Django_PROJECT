from asyncio import create_task
from turtle import home
from django.urls import path

from App import views

urlpatterns = [
    path('',views.home),
    path('create-task/', views.create_task, name='create_task')
]
