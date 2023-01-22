# Generated by Django 3.2.16 on 2023-01-22 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_remove_comment_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0003_liketopiccomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='comments.comment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('owner', 'comment')},
            },
        ),
    ]
