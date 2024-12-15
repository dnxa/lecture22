from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    quality = models.IntegerField()

    def __str__(self):
        return self.name