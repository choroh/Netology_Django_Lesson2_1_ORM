from django.contrib import admin

# Register your models here.
from phones.models import Phone


@admin.register(Phone)
class PoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']