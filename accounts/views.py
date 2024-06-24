from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from . forms import RegisterForm, ProfileForm
from django.contrib import messages
from . models import Profile
from core.models import Video
from django.contrib.auth.models import User
from core.models import Video
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfull Login to Continue!")
            return redirect('login')
        else:
            messages.warning(request, "Something went Wrong")
            return redirect('signup')
    else:
        form = RegisterForm()

    return render(request, 'accounts/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'login successfull')
            return redirect('home')
        else:
            messages.warning(request, 'something went wrong!')
            return redirect('login')
    else:
        return render(request, 'accounts\login.html')

def user_logout(request):
    logout(request)
    messages.info(request, 'Logout successfully')
    return redirect('login')

@login_required
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
        videos = profile.user.videos.all()
    else:
        profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile':profile, "videos":videos})

@login_required
def profile_edit(request):

    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'accounts\edit_profile.html', {'form':form})

    
