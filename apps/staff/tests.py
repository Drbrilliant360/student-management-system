from django.test import TestCase
from apps.accounts.models import User
from .models import StaffProfile


class StaffProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='staff1',
            email='staff@example.com',
            password='testpass123',
            role='staff'
        )
        self.staff = StaffProfile.objects.create(
            user=self.user,
            staff_id='STAFF001',
            department='engineering'
        )
    
    def test_staff_profile_creation(self):
        self.assertEqual(self.staff.staff_id, 'STAFF001')
        self.assertEqual(self.staff.department, 'engineering')
    
    def test_staff_profile_str(self):
        self.assertIn('STAFF001', str(self.staff))
