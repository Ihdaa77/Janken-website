from django.shortcuts import render
from .models import Menu, Category
# Create your views here.

def items(request):
    items = Menu.objects.all()
    Categories = Category.objects.all()

    
    return render(request, 'menu/menu.html', {'items': items, 'Categories': Categories})

