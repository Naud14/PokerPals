# Generated by Django 4.1.6 on 2023-04-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_profile_city_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='Oldenzaal', max_length=150),
        ),
    ]
