# Generated by Django 4.2.6 on 2023-10-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='ac@gmail.com', max_length=255, unique=True),
        ),
    ]
