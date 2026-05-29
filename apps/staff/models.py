from django.db import models
from apps.accounts.models import User
from apps.student.models import Course


class StaffProfile(models.Model):
    DEPARTMENT_CHOICES = [
        ('engineering', 'Engineering'),
        ('science', 'Science'),
        ('arts', 'Arts'),
        ('commerce', 'Commerce'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    staff_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    hire_date = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-hire_date']
    
    def __str__(self):
        return f"{self.staff_id} - {self.user.get_full_name()}"


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    total_marks = models.IntegerField(default=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-due_date']
    
    def __str__(self):
        return f"{self.course.code} - {self.title}"


class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.course.code} - {self.title}"
