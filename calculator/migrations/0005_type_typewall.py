# Generated by Django 3.0.4 on 2020-05-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_norms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='название основного раздела', max_length=100, null=True, verbose_name='Название раздела')),
                ('slug', models.SlugField(blank=True, help_text='название url адреса', null=True, unique=True, verbose_name='URL адрес')),
                ('mobile', models.BooleanField(help_text='поставить галочку если нужно в мобильной версии', verbose_name='Мобильная версия')),
            ],
            options={
                'verbose_name': 'Тип штукатурки',
                'verbose_name_plural': 'Тип штукатурки',
            },
        ),
        migrations.CreateModel(
            name='TypeWall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='название основного раздела', max_length=100, null=True, verbose_name='Название раздела')),
                ('slug', models.SlugField(blank=True, help_text='название url адреса', null=True, unique=True, verbose_name='URL адрес')),
                ('mobile', models.BooleanField(help_text='поставить галочку если нужно в мобильной версии', verbose_name='Мобильная версия')),
            ],
            options={
                'verbose_name': 'Тип поверхности',
                'verbose_name_plural': 'Тип поверхности',
            },
        ),
    ]
