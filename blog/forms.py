from django import forms

class NameForm(forms.Form):
     name = forms.CharField(label="")


"""
from django import forms

class NameForm(forms.Form):
     name = forms.CharField(label="")

一応これでフォームの前にname:がないんだけど...
cssとかjquery使うためのclass指定ができない...
widget_tweaksなるものが必要らしい
参考：https://python.keicode.com/django/form-add-class.php
めんどくさいからdjangoでフォーム使わずにhtmlでinput使う
"""
