from django import forms
from .models import Element

PRODUCT_QUANTITY_CHOICES = Element.objects.all()


class ElementsForm(forms.Form):
    quantity = forms.ModelChoiceField(queryset = PRODUCT_QUANTITY_CHOICES)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class ParametersForm(forms.Form):
    num1 = forms.IntegerField(required=False, initial="0")
    num2 = forms.IntegerField(required=False, initial="0")

class HomeForm(forms.Form):
    num1 = forms.IntegerField(required=False)
    num2 = forms.IntegerField(required=False)