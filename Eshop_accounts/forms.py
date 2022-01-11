from django import forms
from django.contrib.auth.models import User
from django.core import validators


class Login_Form(forms.Form):
    username = forms.CharField(label='نام کاربری',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}))
    password = forms.CharField(label='کلمه عبور',
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد کنید'}))
    remember_me = forms.BooleanField(required=False)
    show_password = forms.BooleanField(required=False,
                                       widget=forms.CheckboxInput(attrs={'onclick': 'reveal()'}),
                                       )

    def clean_username(self):
        user = self.cleaned_data.get('username')
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
                               widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور (حداقل 8 حرف )'}),
                               validators=[
                                   validators.MinLengthValidator(8, message='حداقل تعداد کلمه عبور باید 8 رقم باشد.'),
                               ],
                               )
    re_password = forms.CharField(label='تکرار کلمه عبور',
                                  widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),
                                  )
    show_password = forms.BooleanField(required=False,
                                       label='نمایش رمز عبور',
                                       widget=forms.CheckboxInput(attrs={'style': '''width:auto;
                                                                                  height:auto;
                                                                                  display:inline;''',
                                                                         'class': 'form-check-input',
                                                                         'onclick': 'reveal()'}),
                                       )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('ایمیل وجود دارد.')

        # if len(email) < 6 and email.count('@') != 1:
        #     raise forms.ValidationError('ایمیل معتبر وارد کنید.')
        return email

    def clean_username(self):

        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()

        if exists:
            raise forms.ValidationError('نام کاربری که وارد کردید وجود دارد.')
        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارد.')

        return password


class edit_form(forms.Form):
    first_name = forms.CharField(label='نام',
                                 widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'})
                                 )
    last_name = forms.CharField(label='نام خوانوادگی',
                                widget=forms.TextInput(attrs={'placeholder': 'نام خوانوادگی', 'class': 'form-control'})
                                )
