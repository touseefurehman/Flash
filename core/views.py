from django.shortcuts import render,HttpResponse,redirect
from app.forms import SignUpForm
from app.models import User
# Create your views here.

def signin(request):
    return render(request,'signin.html')
def forget(request):
    return render(request,'forget.html')
def pass_reset(request):
    return render(request,'pass_reset.html')
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
         
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
           
            user = User(first_name=first_name, last_name=last_name, email=email)
            user.save()
            
          
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def rent(request):
    return render(request,'rent.html')

def lend (request):
    return render(request,'lend.html')

def list_an_item(request):
    return render(request,'list_an_item.html')






