# Generated by Django 4.2.7 on 2023-12-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=400)),
                ('image', models.ImageField(upload_to='client/')),
            ],
        ),
    ]
