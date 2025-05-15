from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Project, ProjectOwner
from .serializer import ProjectSerializer

class CreateProjectView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        owner = get_object_or_404(ProjectOwner, user=self.request.user)
        serializer.save(owner=owner)
