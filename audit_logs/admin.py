from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "model_name", "object_id", "timestamp")
    list_filter = ("action", "timestamp")
    search_fields = ("user__username", "model_name", "description")
