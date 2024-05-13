from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect


from django.shortcuts import render
from django.conf import settings
import stripe
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from log.models import bio

User = get_user_model()









def checkout(request):
    return render(request,'checkout.html')



def forget(request):
    if request.method=="POST":
        email = request.POST.get("email")
        if not User.objects.filter(email=email).exists():
            messages.warning(request, "User Not exist in the databasse")
            
        
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
#def withdraw(request):
    #return render(request,'withdraw.html')
# views.py

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    return render(request, 'checkout.html')

def withdraw(request):
    if request.method == 'POST':
        token = request.POST['stripeToken']
        amount = 1000  # $10.00
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Example charge',
                source=token,
            )
        except stripe.error.CardError as e:
            # Handle card error
            pass

        # Handle other exceptions

        return render(request, 'withdraw.html')



def inbox(request):
    return render(request,'inbox.html')
def search(request):
    return render(request,'search.html')


def rental(request):
    return render(request,'rental.html')
def rental_list(request):
    
    return render(request,'rental_list.html')














#def list_an_item(request):
 #   return render(request,'list_an_item.html')