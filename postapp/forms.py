from msilib.schema import RadioButton
from tkinter import Radiobutton
from django import forms
from django.forms import TextInput, Textarea
from . models import Lender

OPTION = (
    ('가전제품', '가전제품'),
    ('잡동사니', '잡동사니'),
    ('주방용품', '주방용품')
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Lender
        fields = ['board_title', 'category_opt', 'imgfile', 'board_content']
    board_title = forms.CharField(label='Title')
    category_opt = forms.ChoiceField(widget = forms.RadioSelect(), choices=OPTION, required=False)
    imgfile = forms.ImageField()
    board_content = forms.CharField(widget=forms.Textarea)
    