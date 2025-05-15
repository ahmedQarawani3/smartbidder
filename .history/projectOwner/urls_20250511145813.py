from django.urls import path

urlpatterns = [
    path('projectowner/projects/add/', CreateProjectView.as_view(), name='add-project'),

]
