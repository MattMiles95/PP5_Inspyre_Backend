# Generated by Django 4.2.20 on 2025-04-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approval_status',
            field=models.IntegerField(choices=[(0, 'Approved'), (1, 'Reported')], default=0),
        ),
    ]
