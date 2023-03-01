from django.db import models
from django.urls import reverse

# Create your models here.
class Plane(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"plane_id": self.id})
    