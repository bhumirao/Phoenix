
from django.db import models

# Create your models here


class postEnquiry(models.Model):
    title = models.CharField(max_length=50)
    type=models.CharField(max_length=20)
    date=models.DateTimeField()
    description = models.TextField()