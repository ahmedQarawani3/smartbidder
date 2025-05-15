from django.urls import path
from . import views
from .views import AddProjectAPIView

urlpatterns = [
    path('projects/add/', AddProjectAPIView.as_view(), name='add-project'),

]
