from django.db import models

# Create your models here.
class UserTable(models.Model):
    user_index = models.AutoField(primary_key=True) # 가입순서
    username = models.CharField(max_length = 20, null=False) # 사용자 이름
    user_id = models.CharField(max_length = 20, null=False, unique=True) # 사용자 ID
    pw = models.CharField(max_length = 20, null=False) # 사용자 PW
    user_email = models.EmailField(max_length=50, null=False)
    register_date = models.DateTimeField() # 등록 날짜