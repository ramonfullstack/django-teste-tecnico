from datetime import datetime
from django.db import models
from company.models import Company
from django.contrib.auth.models import User
from doc.models import Doc  # Import the Doc model

class UserProfile(models.Model):
    email = models.EmailField(max_length=255, unique=True, default="example@gmail.com")
    last_password_reset = models.DateTimeField(default=datetime.now)
    email_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=255, default="xxxxx")
    creation_date = models.DateTimeField(default= datetime.now)
    last_update = models.DateTimeField(auto_now=True)
    original_company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='original_members')
    companies = models.ManyToManyField(Company, related_name='members', null=True, blank=True)
    docs = models.ManyToManyField(Doc, related_name='users', null=True, blank=True)
