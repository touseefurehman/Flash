from django.shortcuts import render

# Create your views here.






def checkout(request):
    return render(request,'checkout.html')

def rental(request):
    return render(request,'rental.html')
def rental_list(request):
    return render(request,'rental_list.html')

def sign(request):
    return render(request,'signin.html')