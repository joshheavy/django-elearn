# Generated by Django 3.0.6 on 2020-07-19 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_subject_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='slug',
        ),
    ]
