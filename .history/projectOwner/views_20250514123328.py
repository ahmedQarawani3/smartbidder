from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Project, ProjectOwner
from .serializer import ProjectSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class CreateProjectView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser]  
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise AuthenticationFailed('User is not authenticated')
        
        owner = get_object_or_404(ProjectOwner, user=self.request.user)
        serializer.save(owner=owner)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectStatusSerializer
from rest_framework import status

class ProjectStatusView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectStatusSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

