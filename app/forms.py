from django import forms
from . models import Posting

class PostForm(forms.ModelForm):
    class Meta:
        model = Posting

        fields = ['board_title', 'board_content']


        labels = {
            'board_title' : 'Title',
            'board_content' : 'Content'
        }


    