from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Resume(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, related_name='resume_author', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = "Тут хранятся резюме"


