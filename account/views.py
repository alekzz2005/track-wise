from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate # Core auth functions
from django.contrib.auth.decorators import login_required # Decorator for access control
from django.contrib import messages # For displaying success/error messages

# Import the custom forms you created
from .forms import CustomUserCreationForm, CustomAuthenticationForm 


# --- REGISTRATION VIEW ---
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user object
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            login(request, user)
            messages.success(request, "Account created successfully! Welcome.")
            return redirect('account:dashboard')
        else:
            # Display errors if the form is invalid (e.g., password too short)
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        # GET request: show an empty form
        form = CustomUserCreationForm()
        
    # Render the registration page, passing the form to the template
    return render(request, 'account/register.html', {'form': form})


# --- LOGIN VIEW ---
def login_view(request):
    if request.method == 'POST':
        # Pass the request and POST data to the AuthenticationForm
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # The form handles authentication; get the authenticated user
            user = form.get_user()
            # Log the user in to establish a session
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('account:dashboard')
        else:
            # Display errors for invalid credentials
            messages.error(request, "Invalid username or password.")
    else:
        # GET request: show an empty form
        form = CustomAuthenticationForm()
        
    # Render the login page, passing the form
    return render(request, 'account/login.html', {'form': form})


# --- LOGOUT VIEW ---
def logout_view(request):
    # End the user session
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('account:login')


# --- DASHBOARD VIEW (Requires Login) ---
@login_required(login_url='account:login') # Ensures users must log in to access this page
def dashboard_view(request):
    # This view is only reached if request.user is authenticated
    return render(request, 'account/dashboard.html')