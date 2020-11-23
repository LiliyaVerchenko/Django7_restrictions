from django.contrib import admin
from advertisements.models import AdvertisementStatusChoices, Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass