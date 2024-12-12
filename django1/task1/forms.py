from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(max_length=8, label="Введите пароль")
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')
    balance = forms.CharField(max_length=8, label='Сколько денег у вас есть на счету?')
    age = forms.CharField(max_length=3, label='Введите возраст')
