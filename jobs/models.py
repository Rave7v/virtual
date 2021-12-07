from django.db import models

# Create your models here.
class Job(models.Model):
    titulo=models.CharField(max_length=70)
    resumen=models.CharField(max_length=200)
    marca=models.CharField(max_length=18)
    image=models.ImageField(upload_to='images/')
    fecha_pub=models.DateTimeField(auto_now_add=True)
    