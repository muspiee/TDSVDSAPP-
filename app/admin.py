from django.contrib import admin
from .models import VDSTDS, sponsers

class VDSTDSAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name')
    search_fields = ('name', 'serial_number')

# Register the custom admin class with the model
admin.site.register(VDSTDS, VDSTDSAdmin)
admin.site.register(sponsers)