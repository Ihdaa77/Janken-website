from .models import *

def get_company_info(request):
    company = Company.objects.all().last()
    return {'company':company}