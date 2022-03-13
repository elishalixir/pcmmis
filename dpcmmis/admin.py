from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserData

# Register your models here.
admin.site.site_header = 'Mercury Management Information System'
admin.site.register(UserData)
admin.site.unregister(Group)