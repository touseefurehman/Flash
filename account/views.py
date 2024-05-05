from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Email has been send to your email address please Activate that')
            fm.save()
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
    return render(request, 'signin.html', {'form': form})



