# kash/userincome/forms.py
from django import forms
from .models import UserIncome

class IncomeForm(forms.ModelForm):
    class Meta:
        model = UserIncome
        fields = ['amount', 'date', 'description', 'source']
