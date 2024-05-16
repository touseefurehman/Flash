from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import RentalItem
from log.models import bio

# Create your views here.



def pdp(request, rental_item_id):
    rental_item = get_object_or_404(RentalItem, pk=rental_item_id)
  
    if request.method == 'POST':
        comment = request.POST.get('comment')

        

    return render(request, 'pdp.html', {'rental_item': rental_item})
