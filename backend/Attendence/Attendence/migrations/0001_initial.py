# Generated by Django 4.2.6 on 2023-10-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('Reg_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('RFID', models.CharField(max_length=40)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('attendence', models.CharField(default='A', max_length=1)),
            ],
        ),
    ]
