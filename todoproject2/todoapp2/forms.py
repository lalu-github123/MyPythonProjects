from django import forms
from .models import TodoModel

class update_form(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['name','priority','date']