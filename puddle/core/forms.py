from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForms(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu usuário",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Seu melhor e-mail",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "confirme sua senha",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )

class LoginForms(AuthenticationForm):  
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu usuário",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )