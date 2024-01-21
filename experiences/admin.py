from django.contrib import admin
from .models import Experience, Perk


# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "address",
        "start",
        "end",
        "host",
        "created_at",
    )
    list_filter = (
        "name",
        "price",
        "address",
        "start",
        "end",
        "host",
        "created_at",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "explanation",
        "created_at",
    )
    list_filter = (
        "name",
        "details",
        "explanation",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
