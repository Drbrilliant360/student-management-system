# 📋 Student Information System - Quick Reference Card

## 🎯 Quick Start (Copy & Paste)

```bash
cd d:\StudentInfoSystem
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py create_sample_data
python manage.py runserver
```

Then open: **http://localhost:8000/**

---

## 🌐 URLs at a Glance

| Page | URL | User |
|------|-----|------|
| Home | `/` | Public |
| Admin | `/admin/` | Admin |
| Login | `/accounts/login/` | Student |
| Signup | `/accounts/signup/` | Public |
| Profile | `/accounts/profile/` | Logged in |
| Student Dashboard | `/student/dashboard/` | Student |
| My Courses | `/student/courses/` | Student |
| My Marks | `/student/marks/` | Student |
| Attendance | `/student/attendance/` | Student |
| My Fees | `/student/fees/` | Student |
| Staff Dashboard | `/staff/dashboard/` | Staff |
| Enter Grades | `/staff/grades/` | Staff |
| Take Attendance | `/staff/attendance/` | Staff |
| Admin Dashboard | `/admin-panel/dashboard/` | Admin |
| Manage Users | `/admin-panel/users/` | Admin |
| Manage Courses | `/admin-panel/courses/` | Admin |
| Reports | `/admin-panel/reports/` | Admin |

---

## 👥 Test Credentials (After Sample Data)

```
Student Login:
  Username: student1
  Password: password123

Staff Login:
  Username: staff1
  Password: password123

Admin: (Create with createsuperuser)
```

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `settings.py` | Project configuration |
| `urls.py` | URL routing |
| `manage.py` | Django CLI |
| `requirements.txt` | Dependencies |
| `README.md` | Full documentation |
| `SETUP_GUIDE.md` | Setup instructions |
| `PROJECT_SUMMARY.md` | Complete overview |

---

## 🗂️ App Directories

```
apps/accounts/     → User auth & profiles
apps/student/      → Student management
apps/staff/        → Staff management
apps/admin_panel/  → Admin system
templates/         → HTML files
static/            → CSS, JS, images
```

---

## 🔧 Common Commands

```bash
# Development
python manage.py runserver

# Database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Testing
python manage.py test
python manage.py create_sample_data

# Production
python manage.py collectstatic
gunicorn student_system.wsgi
```

---

## 🎨 File Structure

```
StudentInfoSystem/
├── apps/
│   ├── accounts/       ← User management
│   ├── student/        ← Student system
│   ├── staff/          ← Staff system
│   └── admin_panel/    ← Admin system
├── student_system/     ← Project settings
├── templates/          ← HTML templates
├── static/             ← CSS, JS, images
├── manage.py
├── requirements.txt
├── README.md
├── SETUP_GUIDE.md
└── PROJECT_SUMMARY.md
```

---

## 🔐 User Roles

| Role | Access |
|------|--------|
| **Student** | Dashboard, courses, marks, attendance, fees |
| **Staff** | Dashboard, courses, grades, attendance |
| **Admin** | Full system access, reports, user mgmt |

---

## 📊 Database Models

- **User** → Authentication & profiles
- **StudentProfile** → Student information
- **Course** → Course details
- **Enrollment** → Student-Course relationship
- **Attendance** → Attendance records
- **Mark** → Grade tracking
- **Fee** → Fee management
- **StaffProfile** → Staff information
- **SystemLog** → Activity logging
- **Report** → Report data

---

## ✨ Features

✅ Role-based authentication
✅ Student dashboard
✅ Staff grading system
✅ Attendance tracking
✅ Fee management
✅ Course enrollment
✅ Admin panel
✅ Responsive design
✅ Sample data creation
✅ Comprehensive testing

---

## 🎯 Next Steps

1. **Setup** → Run quick start commands
2. **Explore** → Visit http://localhost:8000/
3. **Customize** → Edit templates and styles
4. **Test** → Use sample data
5. **Deploy** → Configure for production

---

## 📞 Support

- Check README.md for full documentation
- See SETUP_GUIDE.md for detailed setup
- Review PROJECT_SUMMARY.md for complete overview
- Django docs: https://docs.djangoproject.com/

---

**All set! Happy coding! 🚀**
