from django.db import models

# Create your models here.


class React(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(blank=True, upload_to="photos", null=True)


class Logs(models.Model):
    data = models.ForeignKey(React, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to="logs")
    is_correct = models.BooleanField(default=False)
