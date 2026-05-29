from django.contrib import admin
from .models import StudentProfile, Course, Enrollment, Attendance, Mark, Fee


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'user', 'current_semester', 'gpa', 'status']
    list_filter = ['status', 'current_semester']
    search_fields = ['student_id', 'user__username', 'user__first_name', 'user__last_name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'credits', 'instructor', 'is_active']
    list_filter = ['is_active']
    search_fields = ['code', 'name']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date']
    list_filter = ['enrollment_date']
    search_fields = ['student__student_id', 'course__code']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date', 'is_present']
    list_filter = ['date', 'is_present']
    search_fields = ['student__student_id', 'course__code']


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'mark_type', 'score', 'date']
    list_filter = ['mark_type', 'date']
    search_fields = ['student__student_id', 'course__code']


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['student', 'fee_type', 'amount', 'status', 'due_date']
    list_filter = ['status', 'fee_type', 'due_date']
    search_fields = ['student__student_id']
