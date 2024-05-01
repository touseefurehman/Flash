from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from app.forms import SignUpForm
from app.models import User
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




def edit_item(request):
    return render(request,'edit_item.html')


def my_item(request):
    return render(request,'my_item.html')



def checkout(request):
    return render(request,'checkout.html')



def forget(request):
    return render(request,'forget.html')
def pass_reset(request):
    return render(request,'pass_reset.html')
def home(request):
    return render(request,'home.html')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
         
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
           
            user = User(first_name=first_name, last_name=last_name, email=email)
            user.save()
            
          
            return redirect('rent')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def rent(request):
    return render(request,'rent.html')

def lend (request):
    return render(request,'lend.html')

def list_an_item(request):
    return render(request,'list_an_item.html')



def camera(request):
    return render(request,'search_by_category.html')



def pdp(request):
    return render(request,'pdp.html')

def profile(request):
    return render(request,'profile.html')
def withdraw(request):
    return render(request,'withdraw.html')



def inbox(request):
    return render(request,'inbox.html')
def search(request):
    return render(request,'search.html')
def edit_profile(request):
    return render(request,'edit_profile.html')

def rental(request):
    return render(request,'rental.html')
def rental_list(request):
    return render(request,'rental_list.html')