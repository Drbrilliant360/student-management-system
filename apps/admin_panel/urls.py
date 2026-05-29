from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', views.AdminPanelView.as_view(), name='dashboard'),
    path('users/', views.ManageUsersView.as_view(), name='users'),
    path('courses/', views.ManageCoursesView.as_view(), name='courses'),
    path('courses/add/', views.AddCourseView.as_view(), name='add_course'),
    path('courses/<int:pk>/edit/', views.EditCourseView.as_view(), name='edit_course'),
    path('courses/<int:pk>/delete/', views.DeleteCourseView.as_view(), name='delete_course'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('users/<int:pk>/toggle-active/', views.ToggleUserActiveView.as_view(), name='toggle_active'),
]
