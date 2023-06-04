from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contact_list')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'user_login.html', {'error_message': error_message})
    return render(request, 'user_login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def user_signup(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            error_message = 'Username is already taken'
        else:
            # Create a new user
            user = User.objects.create_user(
                username=username, password=password)
            login(request, user)
            return redirect('contact_list')

    return render(request, 'user_signup.html', {'error_message': error_message})


@login_required(login_url='/login/')
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_list.html', {'contacts': contacts})


@login_required(login_url='/login/')
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        contact = Contact(user=request.user, name=name,
                          email=email, phone=phone)
        contact.save()
        return redirect('contact_list')
    return render(request, 'add_contact.html')


@login_required(login_url='/login/')
def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.save()
        return redirect('contact_list')
    return render(request, 'edit_contact.html', {'contact': contact})


@login_required(login_url='/login/')
def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_contact.html', {'contact': contact})
