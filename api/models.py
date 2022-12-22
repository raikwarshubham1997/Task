from django.db import models

# Create your models here.

class countryDetails(models.Model):
    flag_link = models.ImageField(upload_to='productimage',blank=True, null=True)
    capital = models.CharField(max_length=500)
    largest_city = models.CharField(max_length=300)
    official_languages = models.CharField(max_length=300)
    area_total = models.CharField(max_length=300)
    Population = models.CharField(max_length=300)
    GDP_nominal = models.CharField(max_length=300)
   

