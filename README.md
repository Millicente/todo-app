# Django Todo Application

A production-ready task management web application built with Django, featuring comprehensive user authentication, task organization, automated email notifications, and scheduled reminders.

## 🌐 Live Demo

**[View Live Application](https://todo-app-production-9acb.up.railway.app)**

## 🛠️ Technology Stack

- **Backend:** Django 6.0.2
- **Language:** Python 3.14
- **Database:** PostgreSQL (production), SQLite (development)
- **Task Scheduler:** APScheduler
- **Email:** Django SMTP with Gmail integration
- **Server:** Gunicorn (WSGI)
- **Deployment:** Railway
- **Version Control:** Git/GitHub

## 📁 Project Structure
```
todo-app/
├── tasks/                      # Main application
│   ├── management/            # Custom management commands
│   │   └── commands/
│   │       └── send_reminders.py
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   ├── tasks/
│   │   │   ├── task_list.html
│   │   │   ├── edit_task.html
│   │   │   ├── add_category.html
│   │   │   └── register.html
│   │   └── registration/
│   │       └── login.html
│   ├── models.py              # Data models (Task, Category)
│   ├── views.py               # Application logic
│   ├── forms.py               # Form definitions
│   ├── urls.py                # URL routing
│   └── admin.py               # Admin configuration
├── todoproject/               # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI configuration
├── clock.py                   # Background scheduler
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── Procfile                   # Deployment configuration
├── railway.json               # Railway build configuration
└── README.md                  # This file
```

## ✨ Features

### User Management
- Secure user registration and authentication system
- Password validation and session management
- User-specific task isolation (each user sees only their own tasks)

### Task Management
- Full CRUD operations (Create, Read, Update, Delete)
- Rich task details including title, description, and timestamps
- Task completion tracking with visual indicators
- One-click toggle for marking tasks complete/incomplete

### Category System
- Create custom user-defined categories
- Color-coded categorization for visual organization
- Filter tasks by category
- Unique categories per user

### Due Date Management
- Date and time tracking for tasks
- Automated overdue detection with visual alerts
- Color-coded task cards:
  - 🔴 Red background for overdue tasks
  - 🟡 Yellow background for tasks due today
  - ⬜ Normal for future tasks

### Email Notifications
- Automated email reminders for due and overdue tasks
- SMTP integration with Gmail
- Scheduled daily reminders at 8:00 AM
- Background task processing with APScheduler

## 📋 Prerequisites

- Python 3.10 or higher
- pip package manager
- Virtual environment tool
- PostgreSQL (for production deployment)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Millicente/todo-app.git
cd todo-app
```

### 2. Create Virtual Environment
```bash
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root (optional for local development):
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

### 5. Database Setup
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📧 Email Configuration

To enable email reminders:

1. Generate a Gmail App Password:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2-Step Verification
   - Go to App Passwords
   - Create a new app password for "Mail"

2. Add credentials to environment variables or `settings.py`:
```python
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
```

3. Test email reminders:
```bash
   python manage.py send_reminders
```

## 🎯 Usage

### For Users

1. **Register:** Create a new account at `/register/`
2. **Login:** Access your dashboard at `/accounts/login/`
3. **Create Tasks:** Add tasks with optional categories and due dates
4. **Organize:** Use categories to group related tasks
5. **Track Progress:** Mark tasks complete with one click
6. **Stay Updated:** Receive daily email reminders for due tasks

### For Administrators

- Access admin panel at `/admin/`
- Manage users, tasks, and categories
- View system-wide statistics
- Monitor task completion rates

## 📊 Database Schema

### Task Model
- `user` (ForeignKey to User)
- `title` (CharField)
- `description` (TextField)
- `completed` (BooleanField)
- `category` (ForeignKey to Category)
- `due_date` (DateField)
- `due_time` (TimeField)
- `created_at` (DateTimeField)

### Category Model
- `user` (ForeignKey to User)
- `name` (CharField)
- `color` (CharField - hex color code)

## 🚢 Deployment

The application is deployed on Railway with the following configuration:

### Production Settings
- **Database:** PostgreSQL
- **Static Files:** WhiteNoise middleware
- **Server:** Gunicorn
- **Worker:** APScheduler for background tasks

### Environment Variables (Railway)
```
SECRET_KEY=production-secret-key
DEBUG=False
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DATABASE_URL=auto-configured-by-railway
```

### Deployment Steps

1. Push code to GitHub
2. Connect Railway to repository
3. Add PostgreSQL database
4. Set environment variables
5. Deploy automatically on push

## 🔄 Automated Reminders

The application uses APScheduler to send daily reminder emails:

- **Schedule:** Every day at 8:00 AM
- **Worker Process:** Runs via `clock.py`
- **Command:** `python clock.py`

Manual trigger:
```bash
python manage.py send_reminders
```

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 🔐 Security Features

- CSRF protection enabled
- Password hashing with Django's built-in system
- User authentication required for all task operations
- Environment-based secret key management
- SQL injection protection via ORM

## 🎨 User Interface

- Clean, minimalist design
- Responsive layout
- Color-coded task cards by category
- Visual indicators for task status (overdue, due today, completed)
- Intuitive navigation

## 🐛 Known Issues

None currently. Please report any bugs via GitHub Issues.

## 🔮 Future Enhancements

- [ ] Task priority levels (High, Medium, Low)
- [ ] Task sharing and collaboration features
- [ ] File attachments for tasks
- [ ] Calendar view integration
- [ ] Mobile application (React Native)
- [ ] REST API with Django REST Framework
- [ ] Task templates for recurring tasks
- [ ] Data export (CSV, PDF)
- [ ] Task statistics and analytics dashboard
- [ ] Integration with Google Calendar

## 🤝 Contributing

This is a portfolio project. Feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Millicent**

- GitHub: [@Millicente](https://github.com/Millicente)
- Project Repository: [todo-app](https://github.com/Millicente/todo-app)
- Live Demo: [https://todo-app-production-9acb.up.railway.app](https://todo-app-production-9acb.up.railway.app)

## 🙏 Acknowledgments

- Django documentation and community
- Railway deployment platform
- APScheduler for task scheduling
- Bootstrap for UI components

---

**Built with ❤️ using Django and Python**