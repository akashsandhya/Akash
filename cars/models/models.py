from django.db import models
class Models(models.Model):
    name=models.CharField(max_length=1000)
    price=models.FloatField()
    image=models.CharField(max_length=5000)

# Create your models here.
