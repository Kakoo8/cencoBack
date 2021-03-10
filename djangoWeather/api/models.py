from django.db import models

# Create your models here.
class Weather(models.Model):
        name= models.CharField( max_length=50)
        temp = models.CharField(max_length=50)
        main = models.CharField(max_length=50)
        def __str__(self):
            return str(self.name)
