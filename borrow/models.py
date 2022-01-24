from django.db import models

class Post(models.Model):
    subject = models.CharField()


class Comment(models.Model):
    content = models.CharField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Stuff(models.Model):
    name = models.CharField()
