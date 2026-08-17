from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Название'
    )
    short_description = models.TextField(
        blank=True, 
        verbose_name='Короткое описание'
    )
    long_description = HTMLField(
        blank=True, 
        verbose_name='Длинное описание'
    )
    lng = models.FloatField(
        blank=True, 
        null=True,
        verbose_name='Долгота'
    )
    lat = models.FloatField(
        blank=True, 
        null=True,
        verbose_name='Широта'
    )

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField(
        verbose_name='Картинка',
    )
    position = models.PositiveIntegerField(
        default=0,
        blank=False, 
        null=False,
        verbose_name='Позиция',
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.id} {self.place.title}"