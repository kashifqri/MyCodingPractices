from django.contrib import admin
from contactenquirys.models import contactEnquirys

class contactEnquirys_Admin (admin.ModelAdmin):
    list_display=("name","email","subject","message")

admin.site.register(contactEnquirys,contactEnquirys_Admin)    
# Register your models here.
