from django.shortcuts import render, redirect
from item.models import Categoria, Item
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import SignupForms


def index(request):
    items = Item.objects.filter(foi_vendido=False)[0:6]
    categories = Categoria.objects.all()

    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
        },
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")

    else:
        form = SignupForms()

    return render(request, "core/signup.html", {"form": form})


def logout_view(request):
    logout(request)

    return redirect("/login/")


def usuario_logado(request):
    return render(request, "core/usuario_logado.html", {"user": request.user})
