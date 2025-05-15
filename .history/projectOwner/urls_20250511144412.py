from django.urls import path
from . import views

urlpatterns = [
    path('projects/add/', AddProjectAPIView.as_view(), name='add-project'),

]
