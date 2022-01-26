from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.db.models.fields import CharField, AutoField, DateTimeField, IntegerField


# Create your models here.


class Posting(models.Model):
    # board_id = AutoField(primary_key=True)
    # userID = CharField(max_length=20)
    # board_title = CharField(max_length=50)
    # board_content = CharField(max_length=2000)
    # board_date = DateTimeField(auto_now_add=True)
    # category_opt = CharField(max_length=10)
    # imgfile = models.ImageField(upload_to="")

    l_posting_index = AutoField(primary_key=True)
    title = CharField(max_length=255)
    body = CharField(max_length=255)
    deposit = IntegerField()
    pic = models.ImageField(upload_to="")
    date = DateTimeField(auto_now_add=True)
    category = CharField(max_length=255)
    user = models.ForeignKey("User" , on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        db_table = 'Lender_Post'
        app_label = 'postapp'
        managed = False


class User(models.Model):
    user_index = AutoField(primary_key=True)
    username = CharField(max_length=255)
    user_id = CharField(max_length=255)
    email = CharField(max_length=100)
    addr = CharField(max_length=100)
    pw = CharField(max_length=100)

    class Meta:
        db_table = 'User'
        app_label = 'postapp'
        managed = False


class Object(models.Model):
    object_index = AutoField(primary_key=True)
    object_name = CharField(max_length=255)
    posting  = models.ForeignKey("Posting" , on_delete=models.CASCADE, db_column="l_posting_index")

    class Meta:
        db_table = 'Object'
        app_label = 'postapp'
        managed = False
