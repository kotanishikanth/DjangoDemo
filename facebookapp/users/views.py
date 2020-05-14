from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm

# Create your views here.
def login(request):
    return redirect('authlogin')

def logout(request):
    return redirect('authlogout')

def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        context = { 'title':'register', 'form': form}
        return render(request, 'users/register.html', context)
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():         
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in as { username }')   
            return redirect('login')
        else:
            context = { 'title':'register', 'form': form}
            return render(request, 'users/register.html', context)

def profile(request):
    context = {}
    if request.method == "GET":
        form = UserProfileForm()
        
    elif request.method == "POST":
        form = UserProfileForm(request.POST)
        form.save()
    context['form']= form
    return render(request, 'users/profile.html', context)
