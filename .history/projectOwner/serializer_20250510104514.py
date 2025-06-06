from rest_framework import serializers
from .models import ProjectOwner, User

class ProjectOwnerRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    phone_number = serializers.CharField(max_length=20)
    bio = serializers.CharField(allow_blank=True)
    company_name = serializers.CharField(max_length=255)
    profile_picture = serializers.ImageField(required=False)
    id_card_picture = serializers.ImageField(required=False)
    terms_agreed = serializers.CharField(required=True)   

    class Meta:
        model = ProjectOwner
        fields = ['username', 'email', 'password', 'phone_number', 'bio', 'company_name', 
                  'profile_picture', 'id_card_picture', 'terms_agreed']

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role='owner',
            phone_number=validated_data['phone_number']
        )
        paoject_owner=ProjectOwner.objects.create(
            user=user,
            bio=validated_data['bio'],
            company_name=validated_data['company_name'],
            profile_picture=validated_data.get('profile_picture'),
            id_card_picture=validated_data.get('id_card_picture')
        )

        return         paoject_owner=ProjectOwner.objects.create(

