from django.db import models
from datetime import datetime

class Comment(models.Model):
    post_title = models.CharField(max_length=200)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now) 
    def __str__(self):
        return self.post_title