# quickstart/models.py
from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=70)


class Post(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
