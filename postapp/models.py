from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.db.models.fields import CharField, AutoField, DateTimeField
from django.forms import FileField
# Create your models here.


class Posting(models.Model):
    board_id = AutoField(primary_key=True)
    userID = CharField(max_length=20)
    board_title = CharField(max_length=50)
    board_content = CharField(max_length=2000)
    board_date = DateTimeField(auto_now_add=True)
    category_opt = CharField(max_length=10)
    imgfile = models.ImageField(upload_to="")

    class Meta:
        db_table = 'rental_board'
        app_label = 'app'
        managed = False


