from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timezone = models.CharField(max_length=50, default='-03:00')
    language = models.CharField(max_length=2, choices=[('pt', 'Portuguese'), ('es', 'Spanish'), ('en', 'English')], default='pt')
    invited_users = models.ManyToManyField(User, related_name='invited_companies', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_companies', null=True, blank=True)
