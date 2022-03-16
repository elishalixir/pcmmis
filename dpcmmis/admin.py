from django.contrib import admin
from .models import g_dpcmmis, b_Contact_Person, a_Organization, c_Mercury_Supply_Source, d_Waste, e_Health, f_Challenges
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header = 'Mercury Management Information System'
admin.site.register(g_dpcmmis)
admin.site.register (c_Mercury_Supply_Source)
admin.site.register (e_Health)
admin.site.register (a_Organization)
admin.site.register (d_Waste)
admin.site.register (f_Challenges)
admin.site.register (b_Contact_Person)