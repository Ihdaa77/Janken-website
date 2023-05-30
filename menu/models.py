from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Menu(models.Model):
    name_ar = models.CharField(_("Arabic Name"), max_length=100)
    name_en = models.CharField(_("English Name"), max_length=100)
    Category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='categoryItem', null=True, blank=True)
    SR = models.CharField(_("SR"), max_length=20)
    CAL = models.CharField(_("CAL"), max_length=20, null=True, blank=True)
    def __str__(self):  
        return self.name_en
    

 
    
class Category(models.Model):
    name_ar = models.CharField(_("Arabic Name"), max_length=100)
    name_en = models.CharField(_("English Name"), max_length=100)

    
    def __str__(self):  
        return self.name_en
    


    