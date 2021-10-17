from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo=models.CharField(max_length=70)
    fecha_pub=models.DateTimeField(auto_now_add=True)
    texto=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/')