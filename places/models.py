from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Название'
    )
    description_short = models.TextField(
        blank=True, 
        verbose_name='Короткое описание'
    )
    description_long = models.TextField(
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
    place_image = models.ImageField(
        verbose_name='Ссылка на изображение',
    )

    def __str__(self):
        return f"{self.id} {self.place.title}"