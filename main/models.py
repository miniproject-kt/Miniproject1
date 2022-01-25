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
   borrower_index = models.IntegerField()
   title = models.CharField(max_length=255, null=True)
   #user = models.ForeignKey(User, on_delete=models.CASCADE)

   class Meta:
      db_table = 'Borrower'
      app_label = 'main'
      managed = False

   def __str__(self):
      return self.title

class Lender(models.Model):
   l_posting_index = models.IntegerField(primary_key=True)
   lender_index = models.IntegerField()
   title = models.CharField(max_length=255, null=True)
   rentalfee = models.IntegerField()
   pic = models.CharField(max_length=255, null=True)
   #user = models.ForeignKey(User, on_delete=models.CASCADE)

   class Meta:
      db_table = 'Lender'
      app_label = 'main'
      managed = False

   def __str__(self):
      return self.title