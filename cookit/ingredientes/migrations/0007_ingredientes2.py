# Generated by Django 3.1.2 on 2020-10-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0006_auto_20201004_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comida', models.CharField(max_length=100)),
                ('descripcion2', models.TextField()),
            ],
        ),
    ]
