# Generated by Django 3.2.16 on 2023-01-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='This is my Bio', max_length=500),
        ),
    ]
