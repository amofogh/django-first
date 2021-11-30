from django import forms
from django.contrib.auth.models import User
from django.core import validators


class Login_Form(forms.Form):
    username = forms.CharField(label='نام کاربری',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}))
    password = forms.CharField(label='کلمه عبور',
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد کنید'}))
    remember_me = forms.BooleanField(required=False)

    def clean_username(self):
        user = self.cleaned_data.get('username')
        # user = self.cleaned_data.get('username')
        existence = User.objects.filter(username=user).exists()
        if not existence:
            raise forms.ValidationError('نام کاربری یا کلمه عبور صحیح نمی باشید')
        return user


class Register_Form(forms.Form):
    username = forms.CharField(label='نام کاربری',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'})
                               )
    email = forms.EmailField(label='ایمیل',
                             widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'})
                             )
    first_name = forms.CharField(label='نام',
                                 widget=forms.TextInput(attrs={'placeholder': 'نام'})
                                 )
    last_name = forms.CharField(label='نام خوانوادگی',
                                widget=forms.TextInput(attrs={'placeholder': 'نام خوانوادگی'})
                                )
    password = forms.CharField(label='کلمه عبور',
                               widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
                               validators=[
                                   validators.RegexValidator(r'^\d*$', 'کلمه عبور باید متشکل از عدد و حروف باشد'),
                                   # validators.MinValueValidator(limit_value=8,
                                   #                              message='حداقل تعداد کلمه عبور باید 8 رقم باشد',
                                   #
                                   #
                                   #                              )

                               ]
                               )
    re_password = forms.CharField(label='تکرار کلمه عبور',
                                  widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'})
                                  )

    def clean_re_password(self):
        print('clean started')
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(re_password)
        print(password)
        if password != re_password:
            print('here')
            raise forms.ValidationError('کلمه های عبور مغایرت دارد')

        return password
