from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100, default="")
    dateCreated = models.DateTimeField(auto_now_add=True) # Adiciona a data atual automaticamente]

    def __str__(self): # Mostra o nome em lugar de "User Object"
        return self.username
