# Generated by Django 4.1 on 2022-09-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.CharField(max_length=20)),
                ('fecha_salida', models.CharField(max_length=20)),
                ('cantidad_personas', models.IntegerField()),
            ],
        ),
    ]
