from django.shortcuts import render, redirect
from .models import RentalItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import random
from django.contrib.auth.decorators import login_required
from account.models import bio
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def rental_item_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        daily = request.POST.get('daily')
        weekly = request.POST.get('weekly')
        monthly = request.POST.get('monthly')
        rental_period = request.POST.get('rentalPeriod')
        category = request.POST.get('category')
        market_value = request.POST.get('marketValue')
        quantity = request.POST.get('quantity')
        location = request.POST.get('location')
        description = request.POST.get('profileDescription')
        image = request.FILES.get('image')
        
        # Get the currently logged-in user
        user = request.user
        
        # Create RentalItem object and assign the user
        rental_item = RentalItem.objects.create(
            title=title,
            daily_price=daily,
            weekly_price=weekly,
            monthly_price=monthly,
            rental_period=rental_period,
            category=category,
            market_value=market_value,
            quantity=quantity,
            location=location,
            description=description,
            image=image,
            user=user  # Assign the currently logged-in user
        )
        
        return redirect('search_by_category')
    user_profile = bio.objects.filter(user=request.user).first()
    return render(request, 'list_an_item.html')


def test(request):
    search_query = request.GET.get('q') 
    if search_query:
        rental_items = RentalItem.objects.filter(title__icontains=search_query).order_by('id')
    else:
        rental_items = RentalItem.objects.all().order_by('id')
    
    paginator = Paginator(rental_items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "search_by_category.html", {'page_obj': page_obj})




def login_redirect(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('rental_item_form')
    
def pdp(request, rental_item_id):
    rental_items = RentalItem.objects.all() 
    rental_items = get_object_or_404(RentalItem, pk=rental_item_id)
    return render(request, 'pdp.html', {'rental_item': rental_items})

@login_required
def my_item(request):
    rental_items = RentalItem.objects.all()
    user = request.user 
    return render(request, 'my_item.html', {'rental_items': rental_items, 'user': user})

def edit_item(request):
    
    user_profile = bio.objects.filter(user=request.user).first()
    
    return render(request,'edit_item.html')



def search_by_list(request):
    user_profile = bio.objects.filter(user=request.user).first()

    rental_items = RentalItem.objects.all() 
    return render(request, "search_by_list.html", {'rental_items': rental_items})
