from django import forms


class Login_Form(forms.Form):
    username = forms.CharField(label='نام کاربری',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}))
    password = forms.CharField(label='کلمه عبور',
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد کنید'}))
