from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('project/<str:pk>/', views.single_project, name='single_project'),
]