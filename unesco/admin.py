from django.contrib import admin

# Register your models here.
from .models import Category, State, Region, Iso, Site

admin.site.register(Category)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(Site)