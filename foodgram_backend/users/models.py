from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    """Пользовательская модель"""
    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя",
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия",
        blank=True
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта"
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f"{self.email}"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор"
    )

    def clean(self):
        if self.user == self.author:
            raise ValidationError('Нельзя подписаться на себя самого')

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        unique_together = ['user', 'author']
        constraints = [
            models.CheckConstraint(
                check=~models.Q(
                    user=models.F('author')
                ),
                name='not_self_sub'
            ),
        ]

    def __str__(self):
        return f"{self.user} подписан на {self.author}"
