from pyexpat import model
from django.contrib import admin
from contact_page.models import ContactPage

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display= ('name','email','subject','message')


admin.site.register(ContactPage, contactAdmin)

