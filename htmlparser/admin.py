from django.contrib import admin
from htmlparser.models import RawArchive
# Register your models here.

class RawArchiveAdmin(admin.ModelAdmin): 
    pass 

admin.site.register(RawArchive, RawArchiveAdmin)