# Generated by Django 4.2.6 on 2023-10-25 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attendence', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdata',
            name='image',
        ),
    ]
