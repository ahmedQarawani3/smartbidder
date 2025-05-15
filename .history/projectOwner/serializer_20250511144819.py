# serializers.py
from rest_framework import serializers
from .models import Project, ProjectFile

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['file']


class ProjectSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'funding_goal', 'equity_percentage', 'duration_days', 'files']

    def create(self, validated_data):
        files = validated_data.pop('files', [])
        request = self.context['request']
        owner = request. # تأكد من أن المستخدم مرتبط بـ ProjectOwner

        project = Project.objects.create(owner=owner, **validated_data)

        for file in files:
            ProjectFile.objects.create(project=project, file=file)

        return project
