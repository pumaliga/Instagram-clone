from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatar.jpg')

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=300)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.author}"

