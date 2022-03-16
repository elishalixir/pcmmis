from django.contrib import admin
from .models import dpcmmis
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header = 'Mercury Management Information System'
admin.site.register(dpcmmis)
