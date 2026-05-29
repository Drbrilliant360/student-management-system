from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            role='student'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'student')
        self.assertTrue(self.user.check_password('testpass123'))
    
    def test_user_str(self):
        self.assertIn('Test User', str(self.user))
