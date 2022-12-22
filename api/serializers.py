from rest_framework import serializers
from .models import countryDetails

class CountryDetaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = countryDetails
        fields = ['id', 'flag_link', 'capital', 'largest_city', 'official_languages', 'area_total', 'Population', 'GDP_nominal']