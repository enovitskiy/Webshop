# Generated by Django 3.0.4 on 2020-05-10 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_sorter_sorter'),
        ('calculator', '0003_job_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Norms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norms', models.DecimalField(decimal_places=2, max_digits=10)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_norms', to='calculator.Job')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_norms', to='data.Product')),
            ],
            options={
                'verbose_name': 'Нормы',
                'verbose_name_plural': 'нормы',
                'ordering': ('product',),
            },
        ),
    ]
