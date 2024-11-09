from django import forms


class Contactform(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Введите пароль', widget=forms.PasswordInput)
    age = forms.IntegerField(min_value=18, max_value=99, label="Введите свой возраст")
