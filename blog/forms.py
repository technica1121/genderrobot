from django import forms

class NameForm(forms.Form):
     name = forms.CharField(label='名前')
