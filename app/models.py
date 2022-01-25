from django.db import models

# Create your models here.

class User(models.Model):
    user_index = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255,null=True)
    user_id = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=100, null=True)
    pw = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'User'

class Lender(models.Model):
    l_posting_index =  models.IntegerField(primary_key=True)
    lender_index = models.IntegerField()
    title = models.CharField(max_length=255,null=True)
    category =  models.CharField(max_length=255,null=True)
    body = models.CharField(max_length=255,null=True)
    rentalfee = models.IntegerField()	
    longitude = models.FloatField()
    latitude =models.FloatField()
    object_num	= models.IntegerField()
    pic	= models.CharField(max_length=255,null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Lender'

class Borrower(models.Model):
    b_posting_index =  models.IntegerField(primary_key=True)
    borrower_index = models.IntegerField()	
    title = models.CharField(max_length=255,null=True)
    category =  models.CharField(max_length=255,null=True)
    body = models.CharField(max_length=255,null=True)
    longitude = models.FloatField()
    latitude =models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Borrower'

class Borrower_Chatting(models.Model):
    b_chatting_index = models.IntegerField(primary_key=True)
    #posting_index = models.ForeignKey('Borrower', related_name = 'Borrower', on_delete = models.CASCADE, db_column="posting_index")
    #borrower_index = models.ForeignKey('Borrower', related_name = 'Borrower', on_delete = models.CASCADE, db_column="lender_index")		
    user_index = models.IntegerField()
    object_num = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)
    chatting =  models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'B_Post_Chat'

class Lender_Chatting(models.Model):
    l_chatting_index = models.IntegerField(primary_key=True)
    #posting_index = models.ForeignKey('Lender', related_name = 'Lender', on_delete = models.CASCADE, db_column="posting_index")
    #lender_index = models.ForeignKey('Borrower', related_name = 'Borrower', on_delete = models.CASCADE, db_column="posting_index")	
    user_index = models.IntegerField()
    object_num = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)
    chatting =  models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'L_Post_Chat'

class Object(models.Model):
    object_index = models.IntegerField(primary_key=True)

    object_name	=  models.CharField(max_length=255,null=True)
    borrower_index = models.IntegerField()
    posting_index	=models.IntegerField()
    category = models.CharField(max_length=255,null=True)
    rental_fee	= models.IntegerField()
    longitude =	models.FloatField()
    latitude = models.FloatField()
    lender_index = models.IntegerField()
    class Meta:
        db_table = 'Object'
