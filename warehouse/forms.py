from django import forms


class ProcessReorderForm(forms.Form):
    process_status = forms.BooleanField()