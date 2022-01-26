from django.db import models

class User(models.Model):
    user_index = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,null=True)
    user_id = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=100, null=True)
    addr = models.CharField(max_length=100, null=True)
    pw = models.CharField(max_length=100)
    class Meta:
        db_table = 'User'

class Lender(models.Model):
    l_posting_index =  models.AutoField(primary_key=True)
    lender_index = models.ForeignKey('user', on_delete = models.CASCADE, db_column="user_id")
    title = models.CharField(max_length=255,null=True)
    category =  models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)
    deposit = models.IntegerField(default=0, null=True)	
    pic	= models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Lender_Post'

class Borrower(models.Model):
    b_posting_index =  models.AutoField(primary_key=True)
    borrower_index = models.ForeignKey('user', on_delete = models.CASCADE, db_column="user_id")
    title = models.CharField(max_length=255,null=True)
    category =  models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Borrower_Post'

class Object(models.Model):
    object_index = models.AutoField(primary_key=True)
    object_name	=  models.CharField(max_length=255,null=True)
    #borrower_index = models.IntegerField()
    posting_index = models.ForeignKey('Lender', on_delete = models.CASCADE, db_column="l_posting_index")
    category = models.CharField(max_length=255,null=True)
    deposit	= models.IntegerField()
    lender_index = models.IntegerField()
    class Meta:
        db_table = 'Object'

