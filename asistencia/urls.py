from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.asistencia_list, name='list'),
    path('nueva/', views.asistencia_create, name='create'),
]