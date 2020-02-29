from django.contrib import admin
from .models import *

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name','venue','date','timeStart','timeEnd')
    search_fields = ['name','date']
    


admin.site.register(Events,EventsAdmin)
admin.site.register(tags)
admin.site.register(Ticket)
