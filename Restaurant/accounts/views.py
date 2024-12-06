from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.hashers import check_password

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register.html')
        
        # Hash the password before saving
        hashed_password = make_password(password)

        user = User(username=username, email=email, password=hashed_password)
        user.save()
        messages.success(request, "Registration successful! You can log in now.")
        return redirect('Signin View')
    
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)

            # Verify the password
            if check_password(password, user.password):
                # Handle successful login (e.g., create session)
                return redirect("Items View")  # Replace 'home' with your desired redirect

            else:
                return render(request, "login.html", {"error": "Invalid credentials"})
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "User not found"})

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')


def items(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_category = request.POST.get('food_category')
        food_price = request.POST.get('food_price')
        food_image = request.FILES.get('food_image')

        # Save the data to the model
        # Food.objects.create(
        #     name=food_name,
        #     category=food_category,
        #     price=food_price,
        #     image=food_image
        # )
        return redirect('success')  # Redirect after successful addition

    return render(request, 'items.html')

