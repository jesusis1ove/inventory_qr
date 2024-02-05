from django.contrib import admin

from .models import Meter, MeterVerification, MeterAddress


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'created_at', 'updated_at')


@admin.register(MeterVerification)
class MeterVerificationAdmin(admin.ModelAdmin):
    list_display = ('meter', 'date', 'created_at')


@admin.register(MeterAddress)
class MeterAddressAdmin(admin.ModelAdmin):
    list_display = ('meter', 'address', 'created_at')
