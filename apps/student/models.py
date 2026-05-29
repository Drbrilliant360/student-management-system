from django.db import models
from apps.accounts.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    current_semester = models.IntegerField(default=1)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ], default='active')
    
    class Meta:
        ordering = ['-enrollment_date']
    
    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name()}"


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    credits = models.IntegerField(default=3)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'course')
        ordering = ['-enrollment_date']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.course.code}"


class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='attendance')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('student', 'course', 'date')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.course.code} ({self.date})"


class Mark(models.Model):
    MARK_TYPE_CHOICES = [
        ('assignment', 'Assignment'),
        ('quiz', 'Quiz'),
        ('midterm', 'Midterm'),
        ('final', 'Final Exam'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='marks')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mark_type = models.CharField(max_length=20, choices=MARK_TYPE_CHOICES)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.course.code} ({self.mark_type}): {self.score}"


class Fee(models.Model):
    FEE_TYPE_CHOICES = [
        ('tuition', 'Tuition'),
        ('hostel', 'Hostel'),
        ('library', 'Library'),
        ('lab', 'Lab Fee'),
    ]
    
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='fees')
    fee_type = models.CharField(max_length=20, choices=FEE_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')
    due_date = models.DateField()
    paid_date = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ['-due_date']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.fee_type} ({self.status})"
