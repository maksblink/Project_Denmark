from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm



@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, "items/item_list.html", {"items": items})


@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, "items/item_detail.html", {"item": item})


@login_required
def item_add(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = ItemForm()
    return render(request, "items/item_form.html", {"form": form})


@login_required
def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_detail", item_id=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, "items/item_form.html", {"form": form})


@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("item_list")
    return render(request, "items/item_confirm_delete.html", {"item": item})



def register(request):
    if request.content_type == "application/json":
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Nazwa użytkownika i hasło są wymagane."}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Użytkownik już istnieje."}, status=400)

        user = User(username=username)
        user.set_password(password)
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "message": "Rejestracja zakończona sukcesem"}, status=201)

    else:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("home")
        else:
            form = UserRegisterForm()

        return render(request, "users/register.html", {"form": form})
