from django.urls import path
from . import views

urlpatterns = [
    path('/projects', views.CreateProject.as_view(), name='create_project'),
]
