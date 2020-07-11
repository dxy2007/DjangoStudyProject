from django.db import models


# Create your models here.

class Article(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.TextField()
    Text = models.TextField()

