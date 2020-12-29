from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images")
    bio = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return str(self.user)
