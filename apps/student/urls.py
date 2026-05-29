from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('dashboard/', views.StudentDashboardView.as_view(), name='dashboard'),
    path('courses/', views.MyCoursesView.as_view(), name='courses'),
    path('marks/', views.MyMarksView.as_view(), name='marks'),
    path('attendance/', views.MyAttendanceView.as_view(), name='attendance'),
    path('fees/', views.MyFeesView.as_view(), name='fees'),
]
