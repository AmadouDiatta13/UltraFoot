from django.contrib import admin
from .models import Photo, Contact, Coach, Presentation, Objectif

# Register your models here.
admin.site.register(Photo)
admin.site.register(Coach)
admin.site.register(Contact)
admin.site.register(Presentation)
admin.site.register(Objectif)