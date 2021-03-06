# Generated by Django 2.2.6 on 2020-02-13 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0035_auto_20200213_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('href', models.CharField(blank=True, max_length=100)),
                ('dafilter', models.CharField(blank=True, max_length=100)),
                ('projname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subproj', to='information.Subnavigator')),
                ('subname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='information.Navconstruct')),
            ],
        ),
    ]
