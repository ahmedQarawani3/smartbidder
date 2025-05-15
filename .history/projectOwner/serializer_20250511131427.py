from rest_framework import serializers
from .models import Project, ProjectFile

# Serializer لإنشاء مشروع
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'funding_goal', 'equity_percentage', 'duration_days', 'status']

# Serializer لرفع ملف دعم للمشروع
class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['file_path']
