# Generated by Django 2.1.1 on 2018-09-30 22:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_remove_tweet_tweet_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
