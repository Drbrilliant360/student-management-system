# Django Student Information System - Quick Start Guide

## 🚀 Getting Started

This is a complete Django Student Information System project with a well-organized structure. Follow these steps to get it running:

### Step 1: Set Up Virtual Environment

```bash
cd d:\StudentInfoSystem
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account:
- Username: (e.g., admin)
- Email: (your@email.com)
- Password: (choose a secure password)

### Step 5: Run Development Server

```bash
python manage.py runserver
```

The server will start at: **http://localhost:8000/**

## 📱 Access Points

| Section | URL | User Type |
|---------|-----|-----------|
| Homepage | http://localhost:8000/ | Public |
| Admin Panel | http://localhost:8000/admin/ | Admin |
| Student Login | http://localhost:8000/accounts/login/ | Student |
| Student Dashboard | http://localhost:8000/student/dashboard/ | Student |
| Staff Dashboard | http://localhost:8000/staff/dashboard/ | Staff |
| Admin Dashboard | http://localhost:8000/admin-panel/dashboard/ | Admin |

## 👥 User Roles

### Student
- View enrolled courses
- Check marks and GPA
- View attendance records
- Check fee status
- Update profile

### Staff
- Manage assigned courses
- Enter and track marks
- Take attendance
- View attendance records
- Post announcements and assignments

### Admin
- Manage all users
- Manage courses
- Generate reports
- Monitor system activity
- System configuration

## 📂 Project Structure

```
StudentInfoSystem/
├── apps/
│   ├── accounts/          # Authentication & User Management
│   │   ├── models.py      # Custom User model
│   │   ├── views.py       # Auth views (login, signup, profile)
│   │   ├── urls.py        # Account URLs
│   │   └── admin.py       # Django admin configuration
│   │
│   ├── student/           # Student Management
│   │   ├── models.py      # StudentProfile, Course, Enrollment, etc.
│   │   ├── views.py       # Dashboard and student views
│   │   ├── urls.py        # Student URLs
│   │   └── admin.py       # Django admin configuration
│   │
│   ├── staff/             # Staff Management
│   │   ├── models.py      # StaffProfile, Assignment, Announcement
│   │   ├── views.py       # Staff dashboard and management views
│   │   ├── urls.py        # Staff URLs
│   │   └── admin.py       # Django admin configuration
│   │
│   └── admin_panel/       # Admin Management
│       ├── models.py      # SystemLog, Report models
│       ├── views.py       # Admin views and reports
│       ├── urls.py        # Admin URLs
│       └── admin.py       # Django admin configuration
│
├── student_system/        # Main Django Project
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL router
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
│
├── templates/             # HTML Templates
│   ├── base/
│   │   └── base.html      # Base template with navigation
│   ├── accounts/
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── profile.html
│   ├── student/
│   │   ├── dashboard.html
│   │   ├── my_courses.html
│   │   ├── my_marks.html
│   │   ├── my_attendance.html
│   │   └── my_fees.html
│   ├── staff/
│   │   ├── dashboard.html
│   │   ├── my_courses.html
│   │   ├── enter_grades.html
│   │   ├── take_attendance.html
│   │   └── view_attendance.html
│   ├── admin/
│   │   ├── admin_panel.html
│   │   ├── manage_users.html
│   │   ├── manage_courses.html
│   │   └── reports.html
│   └── home.html          # Landing page
│
├── static/                # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript
│   └── images/            # Images
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore            # Git ignore rules
```

## 🗄️ Database Models

### User Model (apps.accounts.models.User)
- Custom user extending Django's AbstractUser
- Fields: username, email, password, first_name, last_name, role, phone, avatar, is_verified

### StudentProfile (apps.student.models.StudentProfile)
- student_id (unique)
- enrollment_date
- current_semester
- GPA
- status (active, inactive, suspended)

### Course (apps.student.models.Course)
- code (unique)
- name
- description
- credits
- instructor (FK to User)
- is_active

### Enrollment (apps.student.models.Enrollment)
- student (FK to StudentProfile)
- course (FK to Course)
- enrollment_date

### Attendance (apps.student.models.Attendance)
- student (FK to StudentProfile)
- course (FK to Course)
- date
- is_present (boolean)

### Mark (apps.student.models.Mark)
- student (FK to StudentProfile)
- course (FK to Course)
- mark_type (assignment, quiz, midterm, final)
- score
- total_marks
- date

### Fee (apps.student.models.Fee)
- student (FK to StudentProfile)
- fee_type (tuition, hostel, library, lab)
- amount
- amount_paid
- status (unpaid, partial, paid)
- due_date
- paid_date

## 🔧 Common Django Commands

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Create a backup
python manage.py dumpdata > backup.json

# Load backup
python manage.py loaddata backup.json

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

## 🔐 Security Notes

Before deploying to production:

1. Change `SECRET_KEY` in `student_system/settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Set up proper database (PostgreSQL recommended)
6. Configure email settings
7. Enable HTTPS
8. Set up proper CORS headers

## 📦 Dependencies

- Django 4.2.0 - Web framework
- djangorestframework - API support
- Pillow - Image processing
- psycopg2-binary - PostgreSQL adapter
- python-decouple - Configuration management
- celery - Task queue
- redis - Caching and task broker
- gunicorn - Production server

## 🐛 Troubleshooting

### Database Errors
```bash
# Reset database
python manage.py migrate apps.student zero
python manage.py migrate
```

### Missing Static Files
```bash
python manage.py collectstatic --noinput
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

## 📝 Next Steps

1. Test the application by accessing the homepage
2. Create test data through Django admin
3. Customize styling in `static/css/`
4. Add more features as needed
5. Deploy to production server

## 📞 Support

For detailed information, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Project README: README.md

---

**Happy coding!** 🎓
