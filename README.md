# DairyManagement

A Django-based Dairy Management web application for managing milk products, suppliers, customers, and daily transactions. The system includes a user dashboard, admin interface, product management, order tracking, and basic business reporting.

---

## 👥 Team Members

| Name            | USN          |
|----------------|--------------|
| **Girish B**    | 4MC23IS036   |
| **Haneesh H D** | 4MC23IS037   |
| **Dashwanth T R** | 4MC23IS028 |
| **Hruthwik M R** | 4MC23IS043  |

---

## 📝 Project Description

This web application is built using the Django framework and is designed to automate and maintain dairy-related records.  
It includes:

- Product Management (Milk, Ghee, Curds, etc.)
- Order Placement and Management
- Customer & Supplier Management
- Admin Dashboard
- Authentication and Authorization
- SQLite database for development

---

## ⚙️ Technologies Used

| Component        | Technology         |
|-----------------|-------------------|
| Backend         | Python, Django     |
| Frontend        | HTML, CSS, Bootstrap |
| Database        | SQLite (dev) / PostgreSQL (prod recommended) |
| VCS             | Git & GitHub       |
| Web Server (prod) | Gunicorn / Nginx |

---

## 🏛️ System Architecture

User Interface (Browser)
|
Django URL Routing
|
Django Views (Business Logic)
|
Django Models (ORM)
|
Database (SQLite / PostgreSQL)

yaml
Copy code

---

## 🧱 Database Schema (ER Model Overview)

- **Product**
  - id, name, price, quantity, description

- **Customer**
  - id, name, mobile, address

- **Order**
  - id, customer → Foreign Key, product → Foreign Key, quantity, total amount, date

- **User**
  - Uses Django built-in authentication system

---

## 📁 Project Structure

DairyManagement/
│
├── manage.py             # Django's command-line utility
├── db.sqlite3            # SQLite database file (or other database files)
├── requirements.txt      # List of project dependencies
├── README.md             # Project documentation and setup instructions
│
├── DairyManagement/      # ⚙️ Project Configuration Folder (Top-level Django project directory)
│   ├── __init__.py         # Makes the directory a Python package
│   ├── asgi.py             # ASGI configuration for async deployments (modern Django)
│   ├── settings.py         # Main project settings (database, installed apps, templates, static files)
│   ├── urls.py             # Main project URL declarations (routes app-level URLs)
│   └── wsgi.py             # WSGI configuration for deployment
│
└── dairy/                # 🥛 Main Application Folder
    ├── migrations/         # Database migrations (automatically created)
    │   └── __init__.py
    │
    ├── static/             # Application-specific static assets (CSS, JS, images)
    │   ├── css/
    │   └── js/
    │
    ├── templates/          # Application-specific HTML templates
    │   └── dairy/          # Best practice: namespace templates to avoid conflicts
    │       ├── base.html
    │       ├── home.html
    │       └── entry_list.html
    │
    ├── __init__.py           # Makes the directory a Python package
    ├── admin.py              # Configuration for the Django admin interface
    ├── apps.py               # Application configuration class
    ├── models.py             # Database models (defining tables and fields)
    ├── tests.py              # Application-specific tests
    ├── urls.py               # Application-specific URL patterns
    └── views.py              # View functions/classes (handling request/response logic)

---

## 🛠️ Prerequisites

- Python 3.8+ (3.10 recommended)
- Git installed
- Optional: Virtual environment (`venv`)

---

## 🚀 Setup (Development)

Open PowerShell / CMD inside the project folder:

C:\Users\Girish\Desktop\DairyManagement>

r
Copy code

### 1️⃣ Create and Activate Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1   # For PowerShell
2️⃣ Install Dependencies
powershell
Copy code
python -m pip install --upgrade pip
pip install -r requirements.txt
3️⃣ Apply Migrations
powershell
Copy code
python manage.py migrate
4️⃣ Create Admin User
powershell
Copy code
python manage.py createsuperuser
5️⃣ Run Development Server
powershell
Copy code
python manage.py runserver
Open in browser:

cpp
Copy code
http://127.0.0.1:8000/
Admin Panel:

arduino
Copy code
http://127.0.0.1:8000/admin/
🌐 Git Commands (for pushing to GitHub)
bash
Copy code
git init
git add .
git commit -m "Initial Commit"
git branch -M main
git remote add origin <repository URL>
git push -u origin main
If you accidentally tracked the local database, remove it:

bash
Copy code
git rm --cached db.sqlite3
git commit -m "Removed DB file"
git push
🧪 Running Tests
bash
Copy code
python manage.py test
📦 Static Files (for Production)
bash
Copy code
python manage.py collectstatic
🚢 Deployment (Production Recommended)
Step	Tool
Web Server	Gunicorn / Nginx
Hosting	AWS / Railway / DigitalOcean / PythonAnywhere
Database	PostgreSQL

🔮 Future Enhancements
Supplier Ledger with monthly payment auto-calculation

Milk Collection Report PDF Export

Mobile App Integration (Flutter/React Native)

SMS Notifications for daily milk updates

📄 License
Add a license file if required (e.g., MIT License, Apache License).

💬 Contact & Contribution
Open to contributions and feature improvements.

sql
Copy code
Fork → Edit → Commit → Pull Request ✅
🎉 Thank you!
yaml
Copy code
