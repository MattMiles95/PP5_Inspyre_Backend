# Generated by Django 4.2.20 on 2025-05-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='original_author',
            field=models.BooleanField(default=False, help_text='Check this box if you are the original creator of this content.'),
        ),
    ]
