from django import forms
from django.contrib.auth.models import User


class comment_form(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super().__init__()
    #     self.user_id = kwargs.get('user_id')
    #     super(comment_form, self).__init__(*args, **kwargs)

    product_id = forms.IntegerField(
        widget=forms.HiddenInput())
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'ایمیل', 'class': 'form-control', 'style': 'color:black'}))
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'نام و نام خوانوادگی', 'class': 'form-control',
                                      'style': 'color:black'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام', 'class': 'form-control', 'style': 'color:black'}))
