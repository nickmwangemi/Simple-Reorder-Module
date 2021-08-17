from django import forms

class SellForm(forms.Form):
    quantity = forms.IntegerField(label='Enter quantity to sell')

class ReorderForm(forms.Form):
    reorder_quantity = forms.IntegerField(label='Enter quantity to reorder')
