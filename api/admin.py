from django.contrib import admin
from .models import countryDetails
# Register your models here.

@admin.register(countryDetails)
class countryDetailAdmin(admin.ModelAdmin):
    list_display =['id', 'flag_link', 'capital', 'largest_city', 'official_languages', 'area_total', 'Population', 'GDP_nominal']