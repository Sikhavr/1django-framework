from django import forms
from .models import *
class employeeform(forms.ModelForm):
    class Meta:
        model=registration
        fields='__all__'
class studentform2(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
class fileuploadform(forms.Form):
    name=forms.CharField(max_length=20)
    file=forms.FileField()
