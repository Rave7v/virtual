# Generated by Django 3.2.4 on 2021-11-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('resumen', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=18)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
