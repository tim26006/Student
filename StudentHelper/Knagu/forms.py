from django import forms


class Autorization(forms.Form):
    login = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Логин"}))
    password = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Пароль"}))


class Gpt(forms.Form):
    theme = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Введи тему"}))
