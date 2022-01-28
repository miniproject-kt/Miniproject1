from django.db import models

# tables for sample data
'''
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
'''


class User(models.Model):
    user_index = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 20, null=False)
    user_id = models.CharField(max_length = 20, null=False, unique=True)
    pw = models.CharField(max_length = 255, null=False)
    addr = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=False)
    register_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'User'
        managed = False
        

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
        managed = False


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
        managed = False


class Borrower(models.Model):
    b_posting_index =  models.AutoField(primary_key=True)
    borrower_index = models.ForeignKey('user', on_delete = models.CASCADE, db_column="user_id")
    title = models.CharField(max_length=255,null=True)
    category =  models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Borrower_Post'
        managed = False


class Borrower_Chatting(models.Model):
    b_chatting_index = models.AutoField(primary_key=True)
    posting_index = models.ForeignKey('Borrower', on_delete = models.CASCADE, db_column="b_posting_index")
    borrower_index = models.ForeignKey('user', on_delete = models.CASCADE, db_column="user_id")	
    user_index = models.IntegerField()
    object_num = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)
    chatting =  models.TextField(null=True)
    class Meta:
        db_table = 'Borrower_Chatting'
        managed = False
