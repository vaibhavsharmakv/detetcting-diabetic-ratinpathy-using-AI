# Generated by Django 2.0.7 on 2019-11-19 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DDRA', '0011_auto_20191119_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eye_images',
            name='Uid',
        ),
    ]
