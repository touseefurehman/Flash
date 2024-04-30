from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    fm = UserCreationForm()
    return render(request, 'enroll/sign_up.html', {"form":fm})
def checkout(request):
    return render(request,'checkout.html')

def rental(request):
    return render(request,'rental.html')
def rental_list(request):
    return render(request,'rental_list.html')

def sign(request):
    return render(request,'signin.html')