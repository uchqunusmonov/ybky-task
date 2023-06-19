from django.contrib import admin
from .models import Room, Resident, Availability


admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(Availability)
