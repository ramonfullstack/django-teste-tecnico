from django.db import models
from django.contrib.auth.models import User
from company.models import Company


# Create your models here.

class Doc(models.Model):
    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sign_deadline = models.DateTimeField(null=True, blank=True)
    signed = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='docs', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_docs', null=True, blank=True)
