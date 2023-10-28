from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

class Question (models.Model):
    
    question = models.CharField(max_length=200)
    content = models.TextField(max_length=30000)
    created_at = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    author = models.ForeignKey(User, verbose_name=("question_author"), on_delete=models.CASCADE)