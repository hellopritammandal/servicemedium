from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    readonly_fields = ('name', 'email', 'phone_number')

   

admin.site.register(Contact, ContactAdmin)
