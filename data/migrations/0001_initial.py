# Generated by Django 3.0.4 on 2020-03-24 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_video', models.CharField(blank=True, help_text='просто текст про товары', max_length=100, null=True, verbose_name='товары ччч')),
                ('url_video', models.URLField(null=True)),
                ('di_video', models.TextField(null=True)),
                ('date_video', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes_video', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Много товаров',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('likes', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Video')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'Комментарии',
            },
        ),
    ]
