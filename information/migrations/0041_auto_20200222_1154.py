# Generated by Django 2.2.6 on 2020-02-22 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0040_auto_20200222_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='information.Projects'),
        ),
    ]
