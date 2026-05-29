from django.test import TestCase
from apps.accounts.models import User
from .models import StudentProfile, Course, Enrollment


class StudentProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='student1',
            email='student@example.com',
            password='testpass123',
            role='student'
        )
        self.student = StudentProfile.objects.create(
            user=self.user,
            student_id='STU001',
            current_semester=1
        )
    
    def test_student_profile_creation(self):
        self.assertEqual(self.student.student_id, 'STU001')
        self.assertEqual(self.student.status, 'active')
    
    def test_student_profile_str(self):
        self.assertIn('STU001', str(self.student))


class CourseTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            code='CS101',
            name='Introduction to Python',
            credits=3
        )
    
    def test_course_creation(self):
        self.assertEqual(self.course.code, 'CS101')
        self.assertTrue(self.course.is_active)
