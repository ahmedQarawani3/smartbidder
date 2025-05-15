from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, ProjectFile
from .serializers import ProjectSerializer, ProjectFileSerializer

# إنشاء مشروع جديد
class CreateProject(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if request.user.role != 'project_owner':
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        # تأكيد أن المستخدم هو صاحب المشروع
        owner = request.user.projectowner  # assuming that `ProjectOwner` is related to `User`
        
        data = request.data
        data['owner'] = owner.id  # تأكيد أن المشروع يتبع هذا الـ owner
        
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save(owner=owner)
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# رفع ملفات داعمة للمشروع
class UploadProjectFile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({'detail': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user != project.owner.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        
        file_serializer = ProjectFileSerializer(data=request.data)
        
        if file_serializer.is_valid():
            file_serializer.save(project=project)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
