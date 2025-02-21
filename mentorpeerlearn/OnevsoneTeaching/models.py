

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.CharField(max_length=255, blank=True, null=True)  # Allow blank/null
    goals = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    learning_time = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise_areas = models.CharField(max_length=255, blank=True, null=True)
    pricing_per_session = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    certifications = models.FileField(upload_to='certifications/', blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    domains = models.CharField(max_length=255, blank=True, null=True)