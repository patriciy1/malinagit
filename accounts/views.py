from django.shortcuts import render, redirect
from home.models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import OrderForm, CreateUserForm

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('malina_home')
    else:
        form = CreateUserForm()
        context = {'form': form}
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                Customer.objects.create(
                    user=user,
                    email=email,
                )

                messages.success(request, 'Был создан аккаунт для ' + username)
                return redirect('login')

    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('malina_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('malina_home')
            else:
                messages.info(request, 'Никнейм или праоль введены неправильно')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
