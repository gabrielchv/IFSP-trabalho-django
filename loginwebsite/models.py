from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100, default="")

    def __str__(self): # Mostra o nome em lugar de "User Object"
        return self.username
