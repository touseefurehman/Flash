from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout







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


def rent(request):
    return render(request,'rent.html')

def lend (request):
    return render(request,'lend.html')









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














#def list_an_item(request):
 #   return render(request,'list_an_item.html')