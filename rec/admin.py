from django.contrib import admin

# Register your models here.

from .models import item, rating

class itemAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(item)
admin.site.register(rating)

