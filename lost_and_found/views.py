from django.shortcuts import render
from .models import LostItem

def index(request):
    items = LostItem.objects.all().order_by('-date_posted')
    return render(request, 'lost_and_found/index.html', {'items': items})
