# Generated by Django 4.1.6 on 2023-03-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_usersessions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokerpalssessions',
            name='big_blind',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pokerpalssessions',
            name='small_blind',
            field=models.FloatField(),
        ),
    ]
