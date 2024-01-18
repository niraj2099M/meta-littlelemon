from django.contrib import admin
from .models import booking_table,menu_table
# Register your models here.

admin.site.register(booking_table)
admin.site.register(menu_table)
