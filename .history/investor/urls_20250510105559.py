from django.urls import path

urlpatterns = [
    path('register/project-owner', ProjectOwnerRegisterView.as_view(), name='project_owner_register'),
]
