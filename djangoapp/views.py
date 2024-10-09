from .models import Product, customer, Worksite  # Assuming you have a Worksite model
from .forms import ProductForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
# Create your views here.
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')   
def product(request):
    return render(request,'product.html')  
def contact(request):
    return render(request,'contact.html')
def store(request):from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def store(request):
    return render(request, 'store.html')

def error(request):
    return render(request, 'error.html')

@login_required
def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ProductForm()
    return render(request, 'addProduct.html', {'form': form})

@login_required
def viewproduct(request):
    product = Product.objects.all()
    return render(request, 'viewproduct.html', {'products': product})

@login_required
def editProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    else:
        form = ProductForm(instance=product)
    return render(request, 'editProduct.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('viewproduct')
    return render(request, 'delete_product.html', {'product': product})



# ... (keep all your existing views) ...
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import customer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

def accounts_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('user_profile', permanent=True)
            else:
                messages.error(request, 'Invalid username or password')
            return render(request, 'accounts.html')

        elif 'register' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            address = request.POST['address']
            phone = request.POST['phone']
            profile_picture = request.FILES.get('profile_picture')

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    
                    # Handle profile picture
                    if profile_picture:
                        # Generate a unique filename
                        file_name = f"profile_pics/{user.id}_{profile_picture.name}"
                        # Save the file
                        path = default_storage.save(file_name, ContentFile(profile_picture.read()))
                        
                    else:
                        path = None

                    customer.objects.create(
                        user=user, 
                        address=address, 
                        phone=phone,
                        profile_picture=path
                    )
                    messages.success(request, 'Registration successful. Please log in.')
                    return redirect('accounts')
            else:
                messages.error(request, 'Passwords do not match')
            return render(request, 'accounts.html')

    else:
        return render(request, 'accounts.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    try:
        customer_profile = user.customer_profile  # Assuming related_name='customer_profile'
    except customer.DoesNotExist:
        customer_profile = None
    
    # Add a print statement for debugging
    print(f"Customer Profile: {customer_profile}")  # Check if the phone and address are printed correctly
    
    # Get worksites assigned to the user
    worksites = Worksite.objects.filter(user=user)  # Ensure 'user' is the field name that links to the User model
    
    # Add a print statement for debugging
    print(f"Worksites for user {user.username}: {worksites}")

    return render(request, 'user_profile.html', {
        'user': user,
        'customer_profile': customer_profile,
        'worksites': worksites  # Pass worksites to the template
    })

@login_required
def edit_profile(request):
    customer = request.user.customer_profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=customer)
    
    return render(request, 'edit_profile.html', {'form': form})

from .models import Worksite

@login_required
def worksite_detail(request, worksite_id):
    worksite = get_object_or_404(Worksite, id=worksite_id, user=request.user)
    
    return render(request, 'worksite_detail.html', {'worksite': worksite})

@login_required
def worksite_detail(request, worksite_id):
    worksite = get_object_or_404(Worksite, id=worksite_id)
    worksite_images = worksite.images.all()  # Fetch all images related to this worksite

    return render(request, 'worksite_detail.html', {
        'worksite': worksite,
        'worksite_images': worksite_images,
    })