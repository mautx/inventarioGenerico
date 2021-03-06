# Generated by Django 4.0.4 on 2022-06-14 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('unique_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(default='chamaco', max_length=200)),
                ('telephone', models.IntegerField(default=0, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idem', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='nombre_no_registrado', max_length=200)),
                ('unitary_price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('color', models.CharField(default='chamaco', max_length=200)),
                ('width', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('grosor', models.FloatField(default=0)),
                ('propietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputDatos.enterprise')),
            ],
        ),
    ]
