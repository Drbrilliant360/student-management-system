from django.db import models
from apps.accounts.models import User
from apps.student.models import StudentProfile, Course


class SystemLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user} - {self.action} ({self.timestamp})"


class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('attendance', 'Attendance'),
        ('marks', 'Marks'),
        ('fee', 'Fee'),
        ('enrollment', 'Enrollment'),
    ]
    
    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    description = models.TextField(blank=True)
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    generated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-generated_date']
    
    def __str__(self):
        return f"{self.title} ({self.report_type})"
