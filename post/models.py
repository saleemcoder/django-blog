from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    postbody = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title
