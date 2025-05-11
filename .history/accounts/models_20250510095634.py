from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('investor', 'Investor'),
        ('owner', 'Project Owner'),
    )

    username = models.CharField(max_length=150, unique=True)  # الاسم هو نفس اسم المستخدم
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # سيتم تخزينها كـ hash تلقائيًا من create_user()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    language_preference = models.CharField(max_length=10, default='ar')
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role', 'phone_number']

    def __str__(self):
        return f"{self.username} ({self.role})"


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    reviewed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Complaint(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints_made')
    defendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints_received')
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
