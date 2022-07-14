from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    id_link = models.BigAutoField(primary_key=True)
    link = models.URLField(max_length=1000)
    shortlink = models.URLField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['-id_link']
