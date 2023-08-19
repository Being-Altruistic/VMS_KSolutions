from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.

rule = RegexValidator(r'^[A-Za-z]{2}[\s-]{0,1}[0-9]{2}[\s-]{0,1}[A-Za-z]{1,2}[\s-]{0,1}[0-9]{4}$', 'Only Numbers & Characters')

class vms_records(models.Model):
    TWO     = 'TWO WHEELER'
    THREE   = 'THREE WHEELER'
    FOUR    = 'FOUR WHEELER'
      
    TYPE_CHOICES = (
          (TWO, 'Two'),
          (THREE, 'Three'),
          (FOUR, 'Four'),
      )
    
    v_number = models.CharField(max_length=200,null=True,blank=True, validators=[rule], verbose_name="Vehicle Number")
    v_type  = models.CharField(choices=TYPE_CHOICES,max_length=200,null=True,blank=True, verbose_name="Vehicle Type")
    v_model = models.CharField(max_length=500,null=True,blank=True, verbose_name="Vehicle Model")
    v_description = models.TextField(max_length=1000,null=True,blank=True, verbose_name="Vehicle Description")
    created  = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True) 


    def __str__(self):
        return f"VEHICLE NO. >>{self.v_number}"

    class Meta:
        ordering = ('-created',)
    
