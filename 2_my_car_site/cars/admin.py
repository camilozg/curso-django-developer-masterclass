from django.contrib import admin
from cars.models import Car, Review

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CAR INFORMATION', {'fields': ['brand']}),
        ('TIME INFORMATION', {'fields': ['year']})
    ]

admin.site.register(Car, CarAdmin)
admin.site.register(Review)