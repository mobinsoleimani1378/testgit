from random import randint
from uuid import uuid4
from django.shortcuts import render, redirect, reverse
from .forms import EnterPhoneForm, EnterCodeForm, RegisterForm, LoginForm
from .models import Code, MyUser
from django.contrib.auth import login, logout, authenticate


def signup(request):
    user = request.user
    form = RegisterForm(instance=user)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)

    return render(request, 'account_app/signup.html', {'form': form})


def enter_phone(request):
    form = EnterPhoneForm()
    if request.method == "POST":
        form = EnterPhoneForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code = randint(1000, 9999)
            print(code)
            token = str(uuid4())
            Code.objects.create(phone=cd['phone'], code=code, token=token)
            return redirect(reverse('account:enter_code') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid data')

    return render(request, 'account_app/enter_phone.html', {'form': form})


def enter_code(request):
    token = request.GET.get('token')
    form = EnterCodeForm()
    if request.method == 'POST':
        form = EnterCodeForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Code.objects.filter(code=cd['code'], token=token).exists():
                code = Code.objects.get(token=token)
                user, is_created = MyUser.objects.get_or_create(phone=code.phone)
                login(request, user)
                code.delete()
                return redirect('account:signup')
            else:
                form.add_error('code', 'کد را به درستی وارد کنید')
    return render(request, 'account_app/enter_code.html', {'form': form, 'token': token})


def send_again(request):
    new_token = request.GET.get('newcode')
    if new_token:
        new = randint(1000, 9999)
        print('new:', new)
        print('tt:', new_token)
        code = Code.objects.get(token=new_token)
        Code.objects.filter(token=code.token).update(code=new)
        return redirect(reverse('account:enter_code') + f'?token={new_token}')


def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('account:home')
            else:
                form.add_error('phone', 'is not valid')
        else:
            form.add_error('phone', 'is not valid')
    return render(request, 'account_app/login.html', {'form': form})


def home(request):
    return render(request, 'account_app/home.html')
