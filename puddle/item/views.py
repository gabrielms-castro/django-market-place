from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Categoria
from .forms import NewItemForm, EditItemForm


#função para buscarum produto
def items(request):
    query = request.GET.get('query', '')
    categories = Categoria.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(foi_vendido=False)

    if category_id:
        items = items.filter(categoria_id=category_id)

    if query:
        items = items.filter(Q(nome__icontains=query) | Q(descrição__icontains=query))

    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id),
        })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        categoria=item.categoria, foi_vendido=False
    ).exclude(pk=pk)[0:3]

    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


@login_required
def new(request):

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item =form.save(commit=False)
            item.criado_por = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
        
    else:    
        form = NewItemForm()
    

    return render(request, "item/form.html", {"form": form, "title": "Novo produto"})

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, criado_por=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, criado_por=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)
        
    else:    
        form = EditItemForm(instance=item)
    

    return render(request, "item/form.html", {"form": form, "title": "Editar Produto"})
