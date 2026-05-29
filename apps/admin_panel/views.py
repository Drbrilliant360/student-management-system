from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from apps.student.models import StudentProfile, Course
from apps.accounts.models import User
from .models import SystemLog, Report
from .forms import CourseForm
from django.contrib import messages


class AdminPanelView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/admin_panel.html'
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['total_students'] = StudentProfile.objects.count()
        context['total_staff'] = User.objects.filter(role='staff').count()
        context['total_courses'] = Course.objects.count()
        context['total_users'] = User.objects.count()
        context['courses'] = Course.objects.all()
        
        return context


class ManageUsersView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/manage_users.html'
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class ManageCoursesView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/manage_courses.html'
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class ReportsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/reports.html'
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = Report.objects.all()
        return context


class AddCourseView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin/add_course.html'
    success_url = reverse_lazy('admin_panel:courses')
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def form_valid(self, form):
        messages.success(self.request, f'Course {form.cleaned_data["code"]} added successfully!')
        return super().form_valid(form)


class EditCourseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin/edit_course.html'
    success_url = reverse_lazy('admin_panel:courses')
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def form_valid(self, form):
        messages.success(self.request, f'Course {form.cleaned_data["code"]} updated successfully!')
        return super().form_valid(form)


class DeleteCourseView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'admin/delete_course.html'
    success_url = reverse_lazy('admin_panel:courses')
    login_url = 'accounts:login'
    
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, f'Course {course.code} deleted successfully!')
        return super().delete(request, *args, **kwargs)


class ToggleUserActiveView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'accounts:login'

    def test_func(self):
        return self.request.user.role == 'admin'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.is_active = not user.is_active
        user.save()
        status = "reactivated" if user.is_active else "deactivated"
        messages.success(request, f'User {user.username} has been {status}.')
        return redirect('admin_panel:users')
