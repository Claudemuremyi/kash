# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .models import UserProfile
# import uuid
# from django.core.mail import send_mail
# from django.conf import settings

# def home(request):
#     return render(request, 'home.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             full_name = user.get_full_name() or user.username
#             messages.success(request, f'Hello {full_name}, you\'ve successfully logged in.')
#             return redirect('expenses')
#         else:
#             messages.error(request, 'Invalid username or password')
    
#     return render(request, 'authentication/login.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#             return render(request, 'authentication/register.html')
            
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists')
#             return render(request, 'authentication/register.html')
            
#         user = User.objects.create_user(username=username, email=email, password=password)
        
#         token = str(uuid.uuid4())
#         UserProfile.objects.create(
#             user=user,
#             verification_token=token
#         )
        
#         verification_link = f"{request.scheme}://{request.get_host()}/verify/{token}"
#         try:
#             send_mail(
#                 'Verify your email',
#                 f'Please click this link to verify your email: {verification_link}',
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False,
#             )
#         except Exception as e:
#             print(f"Email sending failed: {e}")
        
#         messages.success(request, 'Registration successful. Please check your email to verify your account.')
#         return redirect('login')
        
#     return render(request, 'authentication/register.html')

# def verify_email(request, token):
#     try:
#         profile = UserProfile.objects.get(verification_token=token)
#         profile.email_verified = True
#         profile.verification_token = ''
#         profile.save()
#         messages.success(request, 'Email verified successfully. You can now log in.')
#     except UserProfile.DoesNotExist:
#         messages.error(request, 'Invalid verification token')
#     return redirect('login')



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'authentication/register.html')
            
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, 'Registration successful. Welcome!')
        return redirect('expenses')
        
    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        messages.success(request, f'Hello {username}, you\'ve successfully logged in.')
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Hello {username}, you\'ve successfully logged in.')
            messages.success(request, f'Welcome back, {username}!')
            return redirect('expenses')
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'authentication/login.html')

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')
    return render(request, 'authentication/logout.html')

