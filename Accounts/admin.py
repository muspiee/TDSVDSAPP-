from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'username')
    search_fields = ['username','name']

admin.site.register(Users, UsersAdmin)
admin.site.register(Pot)