from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.db.models.fields import CharField, AutoField, DateTimeField, IntegerField


# Create your models here.


class Posting(models.Model):
    l_posting_index =  models.AutoField(primary_key=True)
    user = models.ForeignKey('user', on_delete = models.CASCADE, db_column="user_id")
    title = models.CharField(max_length=255,null=True)
    category =  models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)
    deposit = models.IntegerField(default=0, null=True)	
    pic	= models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Lender_Post'
        app_label = 'postapp'
        managed = False


class User(models.Model):
    user_index = models.AutoField(primary_key=True) # 가입순서
    username = models.CharField(max_length = 20, null=False) # 사용자 이름
    user_id = models.CharField(max_length = 20, null=False, unique=True) # 사용자 ID
    pw = models.CharField(max_length = 20, null=False) # 사용자 PW
    addr = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=False)
    register_date = models.DateTimeField(auto_now_add=True) # 등록 날짜

    class Meta:
        db_table = 'User'
        app_label = 'postapp'
        managed = False


class Object(models.Model):
    object_index = models.AutoField(primary_key=True)
    object_name	=  models.CharField(max_length=255,null=True)
    #borrower_index = models.IntegerField()
    posting_index = models.ForeignKey('Posting', on_delete = models.CASCADE, db_column="l_posting_index")
    category = models.CharField(max_length=255,null=True)
    deposit	= models.IntegerField()
    lender_index = models.IntegerField()

    class Meta:
        db_table = 'Object'
        app_label = 'postapp'
        managed = False



class Lender_Chatting(models.Model):
    l_chatting_index = models.AutoField(primary_key=True)
    posting_index = models.ForeignKey('Posting', on_delete = models.CASCADE, db_column="l_posting_index")
    lender_index = models.ForeignKey('user', on_delete = models.CASCADE, db_column="user_id")	
    user_index = models.CharField(max_length=20)
    object_num = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)
    chatting =  models.TextField(null=True)
    class Meta:
        db_table = 'Lender_Chatting'
        app_label ='postapp'
        managed = False