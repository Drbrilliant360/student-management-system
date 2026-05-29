# Student Information System - Django Project

A comprehensive Student Information System built with Django for managing academic operations including student profiles, courses, attendance, marks, and fees.

## Features

- **User Management**: Role-based authentication (Student, Staff, Admin)
- **Student Dashboard**: View courses, marks, attendance, and fees
- **Staff Portal**: Manage grades, take attendance, view courses
- **Admin Panel**: System administration, reports, and user management
- **Course Management**: Create and manage courses with enrollment
- **Attendance Tracking**: Mark and view attendance records
- **Grade Management**: Record and track student marks
- **Fee Management**: Track student fees and payments

## Project Structure

```
StudentInfoSystem/
├── student_system/          # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── accounts/           # User authentication and profiles
│   ├── student/            # Student app with models and views
│   ├── staff/              # Staff app
│   └── admin_panel/        # Admin app
├── templates/              # HTML templates organized by app
├── static/                 # Static files (CSS, JS, images)
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone or create the project directory**
   ```bash
   cd StudentInfoSystem
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create and configure .env file** (optional)
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Homepage: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - Student Login: http://localhost:8000/accounts/login/
   - Staff Dashboard: http://localhost:8000/staff/dashboard/

## Apps Overview

### Accounts App
- User authentication and profile management
- Custom User model with role-based access

### Student App
- StudentProfile model
- Course enrollment
- Attendance tracking
- Mark management
- Fee tracking

### Staff App
- Staff profiles
- Course management
- Assignment and announcement creation
- Attendance management

### Admin Panel
- System-wide administration
- User management
- Course management
- Report generation
- System logging

## Database Models

### User (Custom)
- username, email, password
- role (student, staff, admin)
- phone, avatar
- is_verified status

### StudentProfile
- student_id, enrollment_date
- current_semester, GPA
- status (active, inactive, suspended)

### Course
- code, name, description
- credits, instructor
- is_active status

### Enrollment
- student, course relationship
- enrollment_date tracking

### Attendance
- student, course, date
- is_present boolean

### Mark
- student, course, mark_type
- score, total_marks
- date

### Fee
- student, fee_type
- amount, amount_paid
- status (unpaid, partial, paid)

## Usage

### For Students
1. Sign up or login to your account
2. View enrolled courses
3. Check marks and attendance
4. View fee status
5. Update profile information

### For Staff
1. Login with staff credentials
2. Access assigned courses
3. Enter grades for students
4. Take attendance
5. View attendance records

### For Admins
1. Access admin dashboard
2. Manage users (add, edit, delete)
3. Manage courses
4. View system reports
5. Monitor system activity

## API Endpoints (Future)

The project is structured to support REST API through Django REST Framework (installed in requirements.txt).

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

MIT License

## Support

For issues or questions, please contact the development team.

---

**Note**: Update SECRET_KEY in settings.py before deploying to production.
