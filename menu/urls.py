from django.urls import path
from .views import items

app_name = 'menu'

urlpatterns = [
    path('menu/', items,  name='menu_page'),
    # path('albom/', albom,  name='albom'),
    
]