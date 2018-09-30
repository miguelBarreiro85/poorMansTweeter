from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_id = models.AutoField(primary_key=True)
    tweet_author = models.CharField(max_length=50)
    tweet_text = models.CharField(max_length=50)
    tweet_date = models.DateTimeField()