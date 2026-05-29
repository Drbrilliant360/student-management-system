from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.staff.models import StaffProfile
from apps.student.models import StudentProfile

User = get_user_model()

DEMO_PASSWORD = 'demo123456'

STUDENTS = [
    {
        'username': 'demo_student1',
        'email': 'demo.student1@example.com',
        'first_name': 'Alice',
        'last_name': 'Johnson',
        'student_id': 'STU-D001',
        'current_semester': 3,
        'gpa': Decimal('3.85'),
    },
    {
        'username': 'demo_student2',
        'email': 'demo.student2@example.com',
        'first_name': 'Brian',
        'last_name': 'Williams',
        'student_id': 'STU-D002',
        'current_semester': 2,
        'gpa': Decimal('3.42'),
    },
    {
        'username': 'demo_student3',
        'email': 'demo.student3@example.com',
        'first_name': 'Carol',
        'last_name': 'Martinez',
        'student_id': 'STU-D003',
        'current_semester': 4,
        'gpa': Decimal('3.67'),
    },
]

STAFF = [
    {
        'username': 'demo_staff1',
        'email': 'demo.staff1@example.com',
        'first_name': 'David',
        'last_name': 'Chen',
        'staff_id': 'STF-D001',
        'department': 'engineering',
    },
    {
        'username': 'demo_staff2',
        'email': 'demo.staff2@example.com',
        'first_name': 'Emily',
        'last_name': 'Patel',
        'staff_id': 'STF-D002',
        'department': 'science',
    },
    {
        'username': 'demo_staff3',
        'email': 'demo.staff3@example.com',
        'first_name': 'Frank',
        'last_name': 'Okafor',
        'staff_id': 'STF-D003',
        'department': 'commerce',
    },
]

ADMINS = [
    {
        'username': 'demo_admin1',
        'email': 'demo.admin1@example.com',
        'first_name': 'Grace',
        'last_name': 'Thompson',
    },
    {
        'username': 'demo_admin2',
        'email': 'demo.admin2@example.com',
        'first_name': 'Henry',
        'last_name': 'Nguyen',
    },
    {
        'username': 'demo_admin3',
        'email': 'demo.admin3@example.com',
        'first_name': 'Irene',
        'last_name': 'Kowalski',
    },
]


class Command(BaseCommand):
    help = 'Create 3 demo login accounts for students, staff, and admins'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding demo accounts...'))

        for data in STUDENTS:
            user, created = User.objects.update_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'role': 'student',
                    'is_verified': True,
                },
            )
            user.set_password(DEMO_PASSWORD)
            user.save()

            StudentProfile.objects.update_or_create(
                user=user,
                defaults={
                    'student_id': data['student_id'],
                    'current_semester': data['current_semester'],
                    'gpa': data['gpa'],
                    'status': 'active',
                },
            )
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'  {action} student: {data["username"]}')

        for data in STAFF:
            user, created = User.objects.update_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'role': 'staff',
                    'is_verified': True,
                },
            )
            user.set_password(DEMO_PASSWORD)
            user.save()

            StaffProfile.objects.update_or_create(
                user=user,
                defaults={
                    'staff_id': data['staff_id'],
                    'department': data['department'],
                },
            )
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'  {action} staff: {data["username"]}')

        for data in ADMINS:
            user, created = User.objects.update_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'role': 'admin',
                    'is_staff': True,
                    'is_verified': True,
                },
            )
            user.set_password(DEMO_PASSWORD)
            user.save()
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'  {action} admin: {data["username"]}')

        self.stdout.write(self.style.SUCCESS('\nDemo accounts ready. Password for all: demo123456\n'))
        self.stdout.write('Students: demo_student1, demo_student2, demo_student3')
        self.stdout.write('Staff:    demo_staff1, demo_staff2, demo_staff3')
        self.stdout.write('Admins:   demo_admin1, demo_admin2, demo_admin3')
        self.stdout.write('\nLogin at: http://127.0.0.1:8000/accounts/login/')
