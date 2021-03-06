# Generated by Django 2.2.6 on 2020-03-04 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0048_contact_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hreflogo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Textslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textblock', models.TextField(blank=True)),
                ('picture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='information.Pictslider')),
            ],
        ),
    ]
