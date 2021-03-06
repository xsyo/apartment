# Generated by Django 3.1.3 on 2020-11-14 15:16

import apartment.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название квартиры')),
                ('plot', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Площядь')),
                ('floor', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Этаж')),
                ('year_of_construction', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900)], verbose_name='Год постройки')),
                ('room_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Число комнат')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('avatar', models.ImageField(upload_to=apartment.utils.avatar_upload_func, verbose_name='Изоброжение')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название города')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=apartment.utils.img_upload_func, verbose_name='Изоброжение')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apartment.apartment', verbose_name='Квартира')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название района')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='apartment.city', verbose_name='Город')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='apartment.district', verbose_name='Название района'),
        ),
    ]
