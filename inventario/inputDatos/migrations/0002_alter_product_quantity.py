# Generated by Django 4.0.4 on 2022-06-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputDatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]