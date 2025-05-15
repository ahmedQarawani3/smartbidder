from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Project, ProjectOwner
from .serializer import ProjectSerializer

from rest_framework.exceptions import AuthenticationFailed

class CreateProjectView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise AuthenticationFailed('User is not authenticated')
        
        owner = get_object_or_404(ProjectOwner, user=self.request.user)
        serializer.save(owner=owner)

