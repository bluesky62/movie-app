import email
from django import forms

class usersform(forms.Form):
    num1 = forms.CharField(label="value1", required=False, widget=forms.TextInput(attrs={'classs':"form-control"}))
    num2 = forms.CharField(label="value2", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    num3 = forms.CharField(label="value3", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    #email = forms.EmailField()
    #num4 = forms.FileInput(label="value4", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))

