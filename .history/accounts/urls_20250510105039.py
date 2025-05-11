from django.urls import path
from .views import ProjectOwnerRegisterView

urlpatterns = [
    path('register/project-owner/', ProjectOwnerRegisterView.as_view(), name='project_owner_register'),
]
