from django.urls import path
from . import views

urlpatterns = [
    path('projectsظ', views.CreateProject.as_view(), name='create_project'),
]
