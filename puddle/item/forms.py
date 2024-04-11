from django import forms

from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 mx-auto rounded-xl p-1 border"


class NewItemForm(forms.ModelForm):

    class Meta:
        model = Item

        fields = (
            "categoria",
            "nome",
            "descrição",
            "preço",
            "imagem",
        )

        widgets = {
            "categoria": forms.Select(attrs={"class": INPUT_CLASSES}),
            "nome": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "descrição": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "preço": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "imagem": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }


class EditItemForm(forms.ModelForm):

    class Meta:
        model = Item

        fields = (
            "nome",
            "descrição",
            "preço",
            "imagem",
            "foi_vendido",
        )

        widgets = {
            "nome": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "descrição": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "preço": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "imagem": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
