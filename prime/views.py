from django.shortcuts import render, redirect
from django.contrib.auth import login
from app.models import AdminProduct as Product
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'prime/index.html')

def products(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        for i in range(len(products)):
            features = products[i].pro_features
            features = features.split('\n')
            products[i].pro_price_per_user=products[i].pro_price_prime
            products[i].pro_price_plumber=products[i].pro_price_prime
            products[i].pro_price=products[i].pro_price_prime
            for j in range(len(features)):
                features[j] = features[j].strip()
            products[i].pro_features = features
        return render(request, 'prime/products.html', {'products': products})
    else:return redirect('signin')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'prime/profile.html', {'user': request.user})
    else:
        return redirect('signin')
    
def edit_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=request.user.email)
        
        if username:user.username = username
        if firstname:user.first_name = firstname
        if lastname:user.last_name = lastname
        if email:user.email = email
        if password:user.set_password(password)
        user.save()
        if password:login(request, user)
        return redirect("auth_user")
    return render(request, 'prime/editprofile.html', {'user': request.user})