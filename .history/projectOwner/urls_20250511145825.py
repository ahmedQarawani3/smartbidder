from django.urls import path
from .views import CreateProjectView

urlpatterns = [
    path('projectowner/projects/add/', CreateProjectView.as_view(), name='add-project'),

]
