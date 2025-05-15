# views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProjectSerializer
from .models import ProjectOwner
from django.shortcuts import get_object_or_404
class AddProjectAPIView(APIView):
    permission_classes = [IsAuthenticated]


owner = get_object_or_404(ProjectOwner, user=request.user)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            project = serializer.save()
            return Response({"message": "Project created successfully", "id": project.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
