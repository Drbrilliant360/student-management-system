from django.contrib import admin
from .models import SystemLog, Report


@admin.register(SystemLog)
class SystemLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['user__username', 'action']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'report_type', 'generated_by', 'generated_date']
    list_filter = ['report_type', 'generated_date']
    search_fields = ['title']
