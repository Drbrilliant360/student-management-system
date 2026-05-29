from django.contrib import admin
from .models import StaffProfile, Assignment, Announcement


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'user', 'department', 'hire_date']
    list_filter = ['department', 'hire_date']
    search_fields = ['staff_id', 'user__username']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'due_date', 'total_marks', 'created_by']
    list_filter = ['due_date', 'course']
    search_fields = ['title', 'course__code']


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'course__code']
