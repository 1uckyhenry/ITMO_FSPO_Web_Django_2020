from django.contrib import admin
from .models import Owner, Car, License, Possession

admin.site.register(Owner)

admin.site.register(Car)

admin.site.register(License)

admin.site.register(Possession)
