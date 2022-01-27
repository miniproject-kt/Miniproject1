from msilib.schema import RadioButton
from tkinter import Radiobutton
from attr import attrs
from django import forms
from django.forms import TextInput, Textarea
from . models import Posting


OPTION = (
    # ('db' , 'form')
    ('패션의류/잡화', '패션의류/잡화'),
    ('뷰티', '뷰티'),
    ('주방용품', '주방용품'),
    ('홈인테리어', '홈인테리어'),
    ('스포츠/레저', '스포츠/레저'),
    ('문구/오피스', '문구/오피스'),
    ('헬스용품', '헬스용품'),
    ('생활융품', '생활용품'),
    ('반려동물용품', '반려동물용품'),
    ('자동차용품', '자동차용품'),
    ('가전디지털', '가전디지털'),
    ('완구/취미', '완구/취미')
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title', 'category' , 'deposit', 'pic', 'body']

    title = forms.CharField()
    category = forms.ChoiceField(widget = forms.Select(attrs={'class' : 'form-select'}), choices=OPTION)
    deposit = forms.IntegerField()
    pic = forms.ImageField()
    body = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))

    title.widget.attrs.update({'class':'form-control'})

    deposit.widget.attrs.update({'class':'form-control'})
    # pic.widget.attrs.update({'class' : 'form-control'})
    
        