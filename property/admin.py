from django.contrib import admin

from .models import Flat, Complaint, Like


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'price')
    readonly_fields = ('created_at',)
    list_editable = ('new_building',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',
                    'owners_phonenumber', 'owner_pure_phonenumber')
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
