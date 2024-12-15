from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    quality = models.IntegerField()

    '''
    This is the user that created us. We use it to make sure only our creator can see and modify us.
    This is not visible on the creation form it is set automatically when creating through our endpoint.
    I tried to do this using permissions but I dont know if that's possible...
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name