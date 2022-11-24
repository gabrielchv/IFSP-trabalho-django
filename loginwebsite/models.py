from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self): # Mostra o nome em lugar de "User Object"
        return self.username
