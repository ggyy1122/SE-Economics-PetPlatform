from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "created_at"]  #

admin.site.register(Person, PersonAdmin)
