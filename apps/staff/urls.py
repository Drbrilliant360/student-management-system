from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('dashboard/', views.StaffDashboardView.as_view(), name='dashboard'),
    path('courses/', views.MyCourses.as_view(), name='courses'),
    path('grades/', views.EnterGradesView.as_view(), name='grades'),
    path('attendance/', views.TakeAttendanceView.as_view(), name='attendance'),
    path('view-attendance/', views.ViewAttendanceView.as_view(), name='view_attendance'),
]
