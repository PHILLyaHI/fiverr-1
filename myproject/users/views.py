from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from item.models import DeliveryOrder, Item
from users.models import User

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/menu')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


def myaccount(request):
    items = Item.objects.all()
    orders = DeliveryOrder.objects.all()
    return render(request, 'myaccount.html', {"orders": orders, "items": items})

def account(request, user_id):
    user2 = User.objects.get(pk=user_id)
    items = Item.objects.all()
    return render(request, 'account.html', {"items": items, 'user2': user2})