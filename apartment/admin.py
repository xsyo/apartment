from django.contrib import admin

from .models import City, District, Apartment, Image


admin.site.register(City)
admin.site.register(District)
admin.site.register(Apartment)
admin.site.register(Image)
