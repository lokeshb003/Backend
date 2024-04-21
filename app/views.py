from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group

def index(request):
    if request.user.is_authenticated:
        return redirect("auth_user")
    else:
        return redirect('signin')

def auth_user(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='user_admin').exists():
            return redirect('clients')
        elif request.user.groups.filter(name='per_user').exists():
            return redirect('per_user-profile')
        elif request.user.groups.filter(name='plumber').exists():
            return redirect('plumber-profile')
        elif request.user.groups.filter(name='prime').exists():
            return redirect('prime-profile')
              
    else:return redirect('signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect("auth_user")
    elif request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        if User.objects.filter(email=email).exists():messages.info(request, 'Email already exists')
        else:
            if role=='per_user':
                user = User.objects.create_user(username, email, password, is_active=True)
                user = authenticate(request, username=username, password=password)
                group = Group.objects.all().filter(name=role).first()
                user.groups.add(group)
                login(request, user)
            else:
                user = User.objects.create_user(username, email, password)
                user = authenticate(request, username=username, password=password)
                group = Group.objects.all().filter(name=role).first()
                user.groups.add(group)
                user = User.objects.get(username=username)
                user.is_active = False
                user.save()
                return redirect("signin")
            return redirect("auth_user")
        return redirect("signup")
    else:return render(request,'account/signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect("auth_user")
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if '@' in username:username = User.objects.get(email=username).username
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user and User.objects.get(username=username).is_active:
                login(request, user)
                return redirect("auth_user")
            elif User.objects.get(username=username).is_active==False:
                messages.info(request, 'User need to be Approved')
                return redirect("signin")
            else:
                messages.info(request, 'Invalid User Credential')
                return redirect("signin")
        else:
            messages.info(request, 'User Not Found')
            return redirect("signin")
    else:return render(request,'account/signin.html')

def signout(request):
    if request.user.is_authenticated:logout(request)
    return redirect('signin')

def error(request):
    return render(request, 'error.html')

def test(request):
    return render(request, 'test.html')

def delete_account(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        user = User.objects.get(email=request.user.email)
        user.delete()
        return redirect('signin')
    else:
        return redirect('signin')