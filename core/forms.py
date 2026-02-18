from django import forms
from django.contrib.auth import authenticate

class AuthenticationForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            "class": "input",
            "placeholder": "Введите ваше имя пользователя"
        })
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "Введите ваш пароль"
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(
                username=username,
                password=password
            )

            if not user:
                raise forms.ValidationError("Неверный логин или пароль")
            else:
                self.user = user
        
        return cleaned_data                                 