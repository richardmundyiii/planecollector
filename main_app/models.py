from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Pilot(models.Model):
    name: models.CharField(max_length=100)
    rating: models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pilots_detail', kwargs={'pk': self.id})

class Plane(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    pilots = models.ManyToManyField(Pilot)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"plane_id": self.id})

class Maintenance(models.Model):
    date = models.DateField('Appointment Date')
    description = models.TextField(max_length=250)
    faarequired = models.BooleanField(
        default=False,
    )

    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-date']