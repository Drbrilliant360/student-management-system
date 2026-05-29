from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.student.models import StudentProfile, Course, Enrollment, Attendance, Mark, Fee
from apps.staff.models import StaffProfile
from datetime import datetime, timedelta
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))

        # Create users
        try:
            # Create student users
            student1_user = User.objects.create_user(
                username='student1',
                email='student1@example.com',
                password='password123',
                first_name='John',
                last_name='Doe',
                role='student'
            )
            
            student2_user = User.objects.create_user(
                username='student2',
                email='student2@example.com',
                password='password123',
                first_name='Jane',
                last_name='Smith',
                role='student'
            )

            # Create staff user
            staff_user = User.objects.create_user(
                username='staff1',
                email='staff1@example.com',
                password='password123',
                first_name='Dr.',
                last_name='Teacher',
                role='staff'
            )

            self.stdout.write(self.style.SUCCESS('✓ Users created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Users might already exist: {e}'))

        try:
            # Create student profiles
            student1 = StudentProfile.objects.create(
                user=student1_user,
                student_id='STU001',
                current_semester=2,
                gpa=Decimal('3.75')
            )
            
            student2 = StudentProfile.objects.create(
                user=student2_user,
                student_id='STU002',
                current_semester=2,
                gpa=Decimal('3.45')
            )

            self.stdout.write(self.style.SUCCESS('✓ Student profiles created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Student profiles might already exist: {e}'))

        try:
            # Create staff profile
            StaffProfile.objects.create(
                user=staff_user,
                staff_id='STAFF001',
                department='engineering'
            )

            self.stdout.write(self.style.SUCCESS('✓ Staff profile created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Staff profile might already exist: {e}'))

        try:
            # Create courses
            course1 = Course.objects.create(
                code='CS101',
                name='Introduction to Python',
                description='Learn Python basics',
                credits=3,
                instructor=staff_user
            )
            
            course2 = Course.objects.create(
                code='CS102',
                name='Web Development',
                description='Learn web development with Django',
                credits=4,
                instructor=staff_user
            )

            self.stdout.write(self.style.SUCCESS('✓ Courses created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Courses might already exist: {e}'))

        try:
            # Create enrollments
            Enrollment.objects.create(student=student1, course=course1)
            Enrollment.objects.create(student=student1, course=course2)
            Enrollment.objects.create(student=student2, course=course1)

            self.stdout.write(self.style.SUCCESS('✓ Enrollments created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Enrollments might already exist: {e}'))

        try:
            # Create attendance records
            today = datetime.now().date()
            for i in range(10):
                date = today - timedelta(days=i)
                Attendance.objects.create(
                    student=student1,
                    course=course1,
                    date=date,
                    is_present=True if i % 2 == 0 else False
                )

            self.stdout.write(self.style.SUCCESS('✓ Attendance records created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Attendance records might already exist: {e}'))

        try:
            # Create marks
            Mark.objects.create(
                student=student1,
                course=course1,
                mark_type='assignment',
                score=Decimal('18.5'),
                total_marks=Decimal('20')
            )
            
            Mark.objects.create(
                student=student1,
                course=course1,
                mark_type='midterm',
                score=Decimal('42'),
                total_marks=Decimal('50')
            )

            self.stdout.write(self.style.SUCCESS('✓ Marks created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Marks might already exist: {e}'))

        try:
            # Create fees
            due_date = datetime.now().date() + timedelta(days=30)
            Fee.objects.create(
                student=student1,
                fee_type='tuition',
                amount=Decimal('5000'),
                amount_paid=Decimal('2500'),
                status='partial',
                due_date=due_date
            )
            
            Fee.objects.create(
                student=student1,
                fee_type='hostel',
                amount=Decimal('2000'),
                amount_paid=Decimal('0'),
                status='unpaid',
                due_date=due_date
            )

            self.stdout.write(self.style.SUCCESS('✓ Fees created'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Fees might already exist: {e}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Sample data creation completed!\n'))
        self.stdout.write(self.style.WARNING('Login credentials:'))
        self.stdout.write(self.style.WARNING('  Student: student1 / password123'))
        self.stdout.write(self.style.WARNING('  Staff: staff1 / password123'))
