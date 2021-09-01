from django.contrib import admin
from .models import *

admin.site.register(State)
admin.site.register(City)


class PopulationAdmin(admin.ModelAdmin):
    list_display = ('city','population')


admin.site.register(Population, PopulationAdmin)

