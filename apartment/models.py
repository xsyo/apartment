from django.db import models
from django.core.validators import MinValueValidator

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .utils import img_upload_func, avatar_upload_func


class City(models.Model):
    ''' Модель города '''

    name = models.CharField(max_length=50, verbose_name='Название города')

    def __str__(self):
        return self.name


class District(models.Model):
    ''' Модель района '''

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='district', verbose_name='Город')
    name = models.CharField(max_length=100, verbose_name='Название района')

    def __str__(self):
        return f'{self.city.name}, {self.name}'


class Apartment(models.Model):
    ''' Модель квартиры '''

    title = models.CharField(max_length=255, verbose_name='Название квартиры')
    plot = models.IntegerField(verbose_name='Площядь', validators=[MinValueValidator(0)])
    floor = models.IntegerField(verbose_name='Этаж', validators=[MinValueValidator(1)])
    year_of_construction = models.IntegerField(verbose_name='Год постройки', validators=[MinValueValidator(1900)])
    room_count = models.IntegerField(verbose_name='Число комнат', validators=[MinValueValidator(1)])
    address = models.CharField(max_length=255, verbose_name='Адрес')
    price = models.IntegerField(verbose_name='Цена', validators=[MinValueValidator(0)])
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='apartments', verbose_name='Название района')
    avatar = models.ImageField(upload_to=avatar_upload_func, verbose_name='Изоброжение')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    description = models.TextField(verbose_name='Описание')

    avatar_thumbnail = ImageSpecField(source='avatar', processors=[ResizeToFill(570, 350),], options={'quality': 70})

    def __str__(self):
        return self.title

    def get_short_description(self):
        return self.description[:100]

    class Meta:
        ordering = ['-created_at',]

class Image(models.Model):
    ''' Модель изображений '''

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images', verbose_name='Квартира')
    img = models.ImageField(upload_to=img_upload_func, verbose_name='Изоброжение')