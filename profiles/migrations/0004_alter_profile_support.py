# Generated by Django 3.2.16 on 2023-01-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='support',
            field=models.CharField(blank=True, default='Football', max_length=30),
        ),
    ]