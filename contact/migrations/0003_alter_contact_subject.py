# Generated by Django 4.2.7 on 2023-12-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=400),
        ),
    ]