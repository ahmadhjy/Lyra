from django.contrib import admin

from .models import AgoraReferralClick, AgoraReferralConversion


@admin.register(AgoraReferralClick)
class AgoraReferralClickAdmin(admin.ModelAdmin):
    list_display = ("course_slug", "course_title", "ref_id", "clicked_at", "ip_address")
    list_filter = ("course_slug", "clicked_at")
    search_fields = ("course_slug", "course_title", "ref_id")
    readonly_fields = ("ref_id", "clicked_at")


@admin.register(AgoraReferralConversion)
class AgoraReferralConversionAdmin(admin.ModelAdmin):
    list_display = ("event_type", "course_slug", "lyra_ref", "click", "converted_at")
    list_filter = ("event_type", "course_slug", "converted_at")
    search_fields = ("lyra_ref", "course_slug")
    readonly_fields = ("converted_at",)
