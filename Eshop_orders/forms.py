from django import forms


class order_form(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput())
    count = forms.CharField(
        widget=forms.NumberInput(attrs={'min': '1'}),
        initial=1)
