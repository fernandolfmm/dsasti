# Generated by Django 3.1.2 on 2020-10-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0003_platillos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platillos2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePlato', models.CharField(max_length=100)),
                ('ingredientes', models.CharField(max_length=100)),
            ],
        ),
    ]
