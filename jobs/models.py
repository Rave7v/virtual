from django.db import models

# Create your models here.
class Job(models.Model):
    titulo=models.CharField(max_length=70)
    image=models.ImageField(upload_to='images/')
    resumen=models.CharField(max_length=200)