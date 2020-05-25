# Generated by Django 2.2.6 on 2020-03-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0051_textslider_clas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('textblock', models.TextField(blank=True)),
                ('title1', models.CharField(blank=True, max_length=100)),
                ('textblock1', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('answer', models.TextField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]