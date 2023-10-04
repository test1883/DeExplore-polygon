from django.db import models

# Create your models here.


class React(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(blank=True,upload_to="photos", null=True)
