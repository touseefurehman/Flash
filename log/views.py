from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import check_password
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
            return redirect('login')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('search_by_category') 
    
            
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form,})


def bio2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        about = request.POST.get('about')
        number = request.POST.get('number')
        image = request.FILES.get('image')
        
        user = request.user

        user, created = bio.objects.update_or_create(
            user=user,
            defaults={
                'name': name,
                'last_name': last_name,
                'email': email,
                'location': location,
                'about': about,
                'number': number,
                'image': image, 
                
            }
        )
        
        return redirect('search_by_category')
    return render(request, 'setup_proofile.html',  )




def edit_profile(request):
   
        
    return render(request,'edit_profile.html')


    
    
    




@login_required
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    user_profile = bio.objects.filter(user=request.user).first()
    return render(request, "profile.html", {'user_profile': user_profile})




def user_logout(request):
    print(request.user)
    logout(request)
    return redirect('login')







def resetpasswords(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password != confirm_password:
            return HttpResponse("New password and confirm password do not match.")
        
        # Check if the old password matches the password stored in the database
        if not check_password(old_password, request.user.password):
            return HttpResponse("Old password is incorrect.")
        
        request.user.set_password(new_password)
        request.user.save()
        
        return HttpResponse("Password updated successfully.")
