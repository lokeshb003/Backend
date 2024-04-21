import parser
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, Group
from app.models import AdminProduct as Product
import base64

# Create your views here.
def index(request):
    return render(request, 'user_admin/index.html')

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='user_admin').exists():
            return render(request,'user_admin/index.html')
        else:return redirect('auth_user')
    else:return redirect('signin')

def create_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['pro_name']
            price = request.POST['pro_price']
            pro_price_per_user = request.POST['pro_price_per_user']
            pro_price_plumber = request.POST['pro_price_plumber']
            pro_price_prime = request.POST['pro_price_prime']
            description = request.POST['pro_description']
            code = request.POST['pro_code']
            range = request.POST['pro_range']
            features = request.POST['pro_features']
            img = base64.b64encode(request.FILES['pro_image'].read()).decode('utf-8')
            
            product = Product(pro_code=code, pro_name=name, pro_price=price, pro_price_per_user=pro_price_per_user, pro_price_plumber=pro_price_plumber, pro_price_prime=pro_price_prime, pro_description=description, pro_image=img, pro_range=range, pro_features=features)
            product.save()

            return redirect('view-products')
        else:
            return render(request, 'user_admin/createproduct.html')
    else:
        return redirect('signin')

def view_products(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        for i in range(len(products)):
            features = products[i].pro_features
            features = features.split('\n')
            for j in range(len(features)):
                features[j] = features[j].strip()
            products[i].pro_features = features
        # for i in products:
        #     print(i.pro_features)
        return render(request, 'user_admin/viewproduct.html', {'products': products})
    else:
        return redirect('signin')
    
def edit_product(request,pc):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['pro_name']
            price = request.POST['pro_price']
            pro_price_per_user = request.POST['pro_price_per_user']
            pro_price_prime = request.POST['pro_price_prime']
            pro_price_plumber = request.POST['pro_price_plumber']
            code = request.POST['pro_code']
            description = request.POST['pro_description']
            range = request.POST['pro_range']
            features = request.POST['pro_features']
            if 'pro_image' in request.FILES:
                img = base64.b64encode(request.FILES['pro_image'].read()).decode('utf-8')
            else:
                img = Product.objects.get(pro_code=pc).pro_image
            
            product = Product.objects.get(pro_code=pc)
            product.pro_code = code
            product.pro_name = name
            product.pro_price = price
            product.pro_price_per_user = pro_price_per_user
            product.pro_price_prime = pro_price_prime
            product.pro_price_plumber = pro_price_plumber
            product.pro_description = description
            product.pro_image = img
            product.pro_range = range
            product.pro_features = features
            product.save()
            return redirect('view-products')
        
        return render(request, 'user_admin/editproduct.html',{'product': Product.objects.get(pro_code=pc)})
    else:
        return redirect('signin')
    
def delete_product(request,pc):
    if request.user.is_authenticated:
        product = Product.objects.get(pro_code=pc)
        product.delete()
        return redirect('view-products')
    else:
        return redirect('signin')
    

def clients(request):
    if request.user.is_authenticated:
        inactive_clients = {}
        for i in User.objects.all():
            if i.is_active==False and not i.is_superuser:
                inactive_clients[i] = i
        active_clients = {}
        
        for i in User.objects.all():
            if i.is_active==True and not i.is_superuser:
                active_clients[i] = i
        
        return render(request, 'user_admin/clients.html',{'inactive_clients': inactive_clients, 'active_clients': active_clients})
    else:
        return redirect('signin')

def approve_user(request,email):
    if request.user.is_authenticated:
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return redirect('clients')
    else:
        return redirect('signin')
    
def revoke_user(request,email):
    if request.user.is_authenticated:
        user = User.objects.get(email=email)
        user.is_active = False
        user.save()
        return redirect('clients')
    else:
        return redirect('signin')

def remove_user(request,email):
    if request.user.is_authenticated:
        user = User.objects.get(email=email)
        user.delete()
        return redirect('clients')
    else:
        return redirect('signin')
    

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_admin/profile.html', {'user': request.user})
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
        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('user-admin-profile')
    return render(request, 'user_admin/editprofile.html', {'user': request.user})
