from django.contrib import admin
from .models import dpcmmis, ContactPerson, Organization, MercurySupplySource, Waste, ASGMElisha, EnvironmentAndHealth, \
    EnergyConsumptionAndFuelProduction, MercuryAddedProducts, Cement
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header = 'Mercury Management Information System'
admin.site.register(dpcmmis)
admin.site.register(ContactPerson)
admin.site.register(Organization)
admin.site.register(MercurySupplySource)
admin.site.register(EnvironmentAndHealth)
admin.site.register(Waste)
admin.site.register(EnergyConsumptionAndFuelProduction)
admin.site.register(MercuryAddedProducts)
admin.site.register(Cement)
admin.site.register(ASGMElisha)
