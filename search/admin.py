from django.contrib import admin

# Register your models here.

from search.models import Artist,Album,Song

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
