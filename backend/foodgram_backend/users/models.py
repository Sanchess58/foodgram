from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользовательская модель"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    class Meta: 
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
