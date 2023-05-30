from django.urls import path
from .views import company, sign_up, contact, home, album

app_name = 'company'

urlpatterns = [ 
    path('about/', company, name='about'),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('accounts/signup/', sign_up, name='signup'),
    path('album/', album, name='album'),
    ]