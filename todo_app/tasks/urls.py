from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/',  views.update_todo, name='update_task')
]
