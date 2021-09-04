from django.contrib import admin
from .models import *

# admin.site.register(State)
# admin.site.register(City)


# class PopulationAdmin(admin.ModelAdmin):
#     list_display = ('city','population')


# admin.site.register(Population, PopulationAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(LineItem)

