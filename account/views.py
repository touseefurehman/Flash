# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import bio

def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('signin')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Perform validation
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('search_by_category') 
    
            
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form,})


def bio(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        about = request.POST.get('about')
        number = request.POST.get('number')
        user = request.user

        bio = bio.objects.create(
            user=user,
            name=name,
            last_name=last_name,
            email=email,
            location=location,
            about=about,
            number=number,
            image=image
        )
        
        return redirect('search_by_category')
    return render(request, 'setup_proofile.html',  )