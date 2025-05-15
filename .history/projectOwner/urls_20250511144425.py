from django.urls import path
from .views import AddProjectAPIView

urlpatterns = [
    path('projects/add/', AddProjectAPIView.as_view(), name='add-project'),

]
