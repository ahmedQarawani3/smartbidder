from rest_framework import serializers
from .models import Project, ProjectFile

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['file_path']


class ProjectSerializer(serializers.ModelSerializer):
    files = ProjectFileSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Project
        fields = ['title', 'description', 'funding_goal', 'equity_percentage',
                  'duration_days', 'status', 'files']

    def create(self, validated_data):
        files_data = validated_data.pop('files', [])
        project = Project.objects.create(**validated_data)

        for file_data in files_data:
            ProjectFile.objects.create(project=project, **file_data)

        return project
