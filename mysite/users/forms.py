from django import forms
from .models import User
 
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'birthday', 'gender')
        labels = {
            'name': '名前',
            'birthday': '年齢',
            'gender': '性別'
        }
        help_texts = {
            'name': '名前を入力',
            'birthday': '生年月日を選択',
            'gender': '性別を選択'
        }