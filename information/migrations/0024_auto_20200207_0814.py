# Generated by Django 2.2.6 on 2020-02-07 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0023_footercont_subname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footercont',
            name='subname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='information.Navconstruct'),
        ),
    ]
