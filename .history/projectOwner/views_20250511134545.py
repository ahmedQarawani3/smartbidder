from rest_framework.permissions import AllowAny

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProjectSerializer
class CreateProject(APIView):
    permission_classes = [AllowAny]  # السماح للجميع بالوصول

    def post(self, request):
        if request.user.role != 'owner':
            return Response({'error': 'You are not a project owner.'}, status=403)

        # تجهيز البيانات مع إضافة المالك
        data = request.data.copy()

        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save(owner=request.user.)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
