from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Stuff(models.Model):
    name = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

                                                                                  
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    stuff_name = models.CharField(max_length=50, default='')     


class Comment(models.Model):
    content = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
