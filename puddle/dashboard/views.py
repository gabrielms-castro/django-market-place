from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(criado_por=request.user)

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
        },
    )

