from django import forms


class CartItemForm(forms.Form):
    quantity = forms.IntegerField()
