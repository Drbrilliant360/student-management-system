from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils import timezone
from apps.student.models import Course, Enrollment, Attendance, Mark, StudentProfile
from .models import StaffProfile
import uuid


def get_or_create_staff_profile(user):
    """Get or create a StaffProfile for the given user."""
    try:
        return StaffProfile.objects.get(user=user)
    except StaffProfile.DoesNotExist:
        staff_id = f"STAFF-{uuid.uuid4().hex[:8].upper()}"
        return StaffProfile.objects.create(
            user=user,
            staff_id=staff_id
        )


class StaffDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'staff/dashboard.html'
    login_url = 'accounts:login'

    def test_func(self):
        return self.request.user.role == 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff = get_or_create_staff_profile(self.request.user)

        context['staff'] = staff
        context['courses'] = Course.objects.filter(instructor=self.request.user)

        return context


class MyCourses(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'staff/my_courses.html'
    context_object_name = 'courses'

    def test_func(self):
        return self.request.user.role == 'staff'

    def get_queryset(self):
        return Course.objects.filter(instructor=self.request.user)


class EnterGradesView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'staff/enter_grades.html'

    def test_func(self):
        return self.request.user.role == 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(instructor=self.request.user)
        course_id = self.request.GET.get('course') or self.request.POST.get('course')
        if course_id:
            context['selected_course'] = get_object_or_404(Course, pk=course_id, instructor=self.request.user)
            context['students'] = Enrollment.objects.filter(course_id=course_id).select_related('student__user')
        return context

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get('course')
        course = get_object_or_404(Course, pk=course_id, instructor=request.user)
        students = Enrollment.objects.filter(course=course).select_related('student__user')

        for enrollment in students:
            student = enrollment.student
            for mark_type in ['assignment', 'quiz', 'midterm', 'final']:
                score_key = f'score_{student.id}_{mark_type}'
                total_key = f'total_{student.id}_{mark_type}'
                if score_key in request.POST:
                    score = request.POST.get(score_key)
                    total = request.POST.get(total_key, 100)
                    if score:
                        Mark.objects.update_or_create(
                            student=student,
                            course=course,
                            mark_type=mark_type,
                            defaults={'score': score, 'total_marks': total}
                        )
        messages.success(request, f'Grades saved for {course.name}.')
        return redirect('staff:grades')


class TakeAttendanceView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'staff/take_attendance.html'

    def test_func(self):
        return self.request.user.role == 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(instructor=self.request.user)
        course_id = self.request.GET.get('course')
        date_str = self.request.GET.get('date')
        if course_id and date_str:
            context['selected_course'] = get_object_or_404(Course, pk=course_id, instructor=self.request.user)
            context['selected_date'] = date_str
            context['students'] = Enrollment.objects.filter(course_id=course_id).select_related('student__user')
        return context

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get('course')
        date = request.POST.get('date')
        course = get_object_or_404(Course, pk=course_id, instructor=request.user)

        if not date:
            messages.error(request, 'Please select a date.')
            return redirect('staff:attendance')

        students = Enrollment.objects.filter(course=course).select_related('student__user')
        for enrollment in students:
            student = enrollment.student
            is_present = request.POST.get(f'present_{student.id}') == 'on'
            Attendance.objects.update_or_create(
                student=student,
                course=course,
                date=date,
                defaults={'is_present': is_present}
            )
        messages.success(request, f'Attendance recorded for {course.name} on {date}.')
        return redirect('staff:attendance')


class ViewAttendanceView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'staff/view_attendance.html'

    def test_func(self):
        return self.request.user.role == 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(instructor=self.request.user)
        course_id = self.request.GET.get('course')
        if course_id:
            context['selected_course'] = get_object_or_404(Course, pk=course_id, instructor=self.request.user)
            context['attendance_records'] = Attendance.objects.filter(
                course_id=course_id
            ).select_related('student__user').order_by('-date', 'student__student_id')
        return context
