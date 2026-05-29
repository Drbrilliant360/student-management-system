from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import StudentProfile, Enrollment, Attendance, Mark, Fee
import uuid


def get_or_create_student_profile(user):
    """Get or create a StudentProfile for the given user."""
    try:
        return StudentProfile.objects.get(user=user)
    except StudentProfile.DoesNotExist:
        student_id = f"STU-{uuid.uuid4().hex[:8].upper()}"
        return StudentProfile.objects.create(
            user=user,
            student_id=student_id
        )


class StudentDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'student/dashboard.html'
    login_url = 'accounts:login'

    def test_func(self):
        return self.request.user.role == 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = get_or_create_student_profile(self.request.user)

        context['student'] = student
        context['enrollments'] = Enrollment.objects.filter(student=student)
        context['attendance'] = Attendance.objects.filter(student=student)
        context['marks'] = Mark.objects.filter(student=student)
        context['fees'] = Fee.objects.filter(student=student)

        return context


class MyCoursesView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'student/my_courses.html'
    context_object_name = 'courses'

    def test_func(self):
        return self.request.user.role == 'student'

    def get_queryset(self):
        student = get_or_create_student_profile(self.request.user)
        return Enrollment.objects.filter(student=student)


class MyMarksView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'student/my_marks.html'

    def test_func(self):
        return self.request.user.role == 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = get_or_create_student_profile(self.request.user)
        context['marks'] = Mark.objects.filter(student=student)
        return context


class MyAttendanceView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'student/my_attendance.html'

    def test_func(self):
        return self.request.user.role == 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = get_or_create_student_profile(self.request.user)
        context['attendance'] = Attendance.objects.filter(student=student)
        return context


class MyFeesView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'student/my_fees.html'

    def test_func(self):
        return self.request.user.role == 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = get_or_create_student_profile(self.request.user)
        context['fees'] = Fee.objects.filter(student=student)
        return context
