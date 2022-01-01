from django import forms
from django.core import validators


class contact_us_form(forms.Form):
    full_name = forms.CharField(max_length=150,
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'نام و نام خوانوادگی', 'class': 'form-control'}))
    email = forms.EmailField(max_length=150,
                             required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'form-control'}))
    subject = forms.CharField(max_length=200,
                              required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'موضوع', 'class': 'form-control'}),
                              )
    text = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'متن پیام', 'class': 'form-control', 'rows': 8}),
    )

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) < 10:
            raise forms.ValidationError('موضوع باید حداقل 10 حرف باشد.')
        return subject

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 20:
            raise forms.ValidationError('متن پیام باید حداقل 20 حرف باشد.')
        return text
