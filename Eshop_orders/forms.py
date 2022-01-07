import datetime

from django import forms
from django.core.exceptions import ValidationError
from Eshop_orders.models import discount


class order_form(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput())
    count = forms.CharField(
        widget=forms.NumberInput(attrs={'min': '1'}),
        initial=1)


class discount_form(forms.Form):
    code = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'placeholder': 'کد تخفیف خود را وارد نمایید ...'}),
                           )
