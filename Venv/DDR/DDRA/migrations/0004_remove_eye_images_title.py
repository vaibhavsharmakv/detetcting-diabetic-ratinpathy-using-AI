# Generated by Django 2.0.7 on 2019-11-17 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DDRA', '0003_auto_20191117_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eye_images',
            name='title',
        ),
    ]
