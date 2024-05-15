from django.shortcuts import render, redirect
from .models import RentalItem
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from log.models import bio
from django.core.paginator import Paginator


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
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, "search_by_category.html", {'page_obj': page_obj})
    else:
        # Otherwise, return the full HTML page
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
    user = request.user 
    rental_items = RentalItem.objects.filter(user=user)
    user_profile = bio.objects.filter(user=request.user).first()

    return render(request, 'my_item.html', {'rental_items': rental_items, 'user': user})




























@login_required
def edit_item(request, item_id):
    rental_item = get_object_or_404(RentalItem, pk=item_id)
    rental_item = RentalItem.objects.filter(user=request.user).first()

    if request.method == 'POST':

        title = request.POST.get('title')
        daily_price = request.POST.get('daily_price')
        weekly_price = request.POST.get('weekly_price')
        monthly_price = request.POST.get('monthly_price')
        rental_period = request.POST.get('rental_period')
        category = request.POST.get('category')
        market_value = request.POST.get('market_value')
        quantity = request.POST.get('quantity')
        location = request.POST.get('location')
        description = request.POST.get('description')
        

        rental_item.title = title
        rental_item.daily_price = daily_price
        rental_item.weekly_price = weekly_price
        rental_item.monthly_price = monthly_price
        rental_item.rental_period = rental_period
        rental_item.category = category
        rental_item.market_value = market_value
        rental_item.quantity = quantity
        rental_item.location = location
        rental_item.description = description
        

        rental_item.save()
        

        return redirect('my_item')

    return render(request, 'edit_item.html', {'rental_item': rental_item})









def search_by_list(request):
    user_profile = bio.objects.filter(user=request.user).first()

    rental_items = RentalItem.objects.all() 
    return render(request, "search_by_list.html", {'rental_items': rental_items} , {'user_profile': user_profile})



def delete_item(request, item_id):
    rental_item = get_object_or_404(RentalItem, id=item_id)
    rental_item.delete()
    return redirect('my_item')


