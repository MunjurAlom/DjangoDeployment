# Generated by Django 4.2.7 on 2023-12-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.TextField(max_length=700)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=700)),
            ],
        ),
    ]
