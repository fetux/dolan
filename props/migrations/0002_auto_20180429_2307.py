# Generated by Django 2.0.3 on 2018-04-29 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prop',
            name='price',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Precio (opcional)'),
        ),
    ]
