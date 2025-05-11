from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectOwnerRegisterSerializer

class ProjectOwnerRegisterView(APIView):
    def post(self, request):
        serializer = ProjectOwnerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if not request.data.get('terms_agreed'):
                return Response({'error': 'You must agree to the terms and conditions.'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Project owner registered successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
