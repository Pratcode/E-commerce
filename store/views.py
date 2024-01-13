from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib import messages
from django.contrib.auth.models import User,auth


def page1_view(request):
    product_item = Product.objects.all()
    return render(request, 'page1.html', {'product_item': product_item})


def cart_list(request):
    if request.user.is_authenticated:
        obj_cart = Cart.objects.filter(user_owner=request.user)
        return render(request, 'cart_list.html', {'obj_cart': obj_cart})


def cart_view(request, id):
    if request.user.is_authenticated:
        payment = request.POST['payment']
        obj = Cart(user_owner_id=request.user.id, product_item_id=id, payment=payment)
        obj.save()
        return redirect('cart_list')


def page3_view(request, id):
    obj = Product.objects.get(id=id)
    return render(request, 'page3.html', {'x': obj})


def delete(request, id):
    obj = Cart.objects.get(id=id)
    obj.delete()
    return redirect('cart_list')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching')

    return render(request, 'Register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('page1_name')
        else:
            messages.info(request, 'user does not exist')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('page1_name')

