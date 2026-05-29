from django.test import TestCase
from apps.accounts.models import User
from .models import SystemLog


class SystemLogTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin1',
            email='admin@example.com',
            password='testpass123',
            role='admin'
        )
        self.log = SystemLog.objects.create(
            user=self.user,
            action='User Login',
            description='Admin user logged in'
        )
    
    def test_system_log_creation(self):
        self.assertEqual(self.log.action, 'User Login')
        self.assertEqual(self.log.user, self.user)
