from django.db import models
from django.forms.fields import URLField
from django.contrib.auth.models import User


class Link(models.Model):
    link = models.URLField(max_length=1000)
    shortlink = models.URLField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
