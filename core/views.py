from django.shortcuts import render

# Create your views here.

def sign(request):
    return render(request,'signin.html')
def forget(request):
    return render(request,'forget.html')
def pass_reset(request):
    return render(request,'pass_reset.html')
def home(request):
    return render(request,'home.html')
