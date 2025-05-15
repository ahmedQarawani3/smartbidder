from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.CreateProject.as_view(), name='create_project'),
    path('projects/<int:project_id>/upload-file/', views.UploadProjectFile.as_view(), name='upload_project_file'),
]
