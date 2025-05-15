from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, ProjectFile
from .serializer import ProjectSerializer, ProjectFileSerializer
class CreateProject(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if request.user.role != 'project_owner':
            return Response({'error': 'You are not a project owner.'}, status=403)

        # تجهيز البيانات مع إضافة المالك
        data = request.data.copy()
        data['owner'] = request.user.projectowner.id

        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save(owner=request.user.projectowner)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
