from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "activity_type", "duration_minutes", "performed_at")
    search_fields = ("activity_type",)
