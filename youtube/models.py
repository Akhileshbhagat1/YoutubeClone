from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    path = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


