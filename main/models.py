from django.db import models

class User(models.Model):
   user_index = models.IntegerField(primary_key=True)
   username = models.CharField(max_length=255, null=True)

   class Meta:
      db_table = 'User'
      app_label = 'main'
      managed = False
   
   def __str__(self):
      return self.user_name

class Borrower(models.Model):
   b_posting_index = models.IntegerField(primary_key=True)
   title = models.CharField(max_length=255, null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

   class Meta:
      db_table = 'Borrower_Post'
      app_label = 'main'
      managed = False

   def __str__(self):
      return self.title

class Lender(models.Model):
   l_posting_index = models.IntegerField(primary_key=True)
   title = models.CharField(max_length=255, null=True)
   deposit = models.IntegerField()
   pic = models.CharField(max_length=255, null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

   class Meta:
      db_table = 'Lender_Post'
      app_label = 'main'
      managed = False

   def __str__(self):
      return self.title