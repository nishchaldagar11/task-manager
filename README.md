
<h1 align="center">🚀 Task Management System</h1>

<p align="center">
  A modern full-stack web application to manage daily tasks efficiently — built with Flask & MySQL
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-red?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-Design-blue?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/MVC-Architecture-success?style=for-the-badge" />
</p>

---

## 📌 Project Overview

**Task Management System** is a full-stack web application designed to manage and track tasks efficiently.

It supports **multi-user authentication**, **role-based access control**, and a complete **task lifecycle** — including creation, editing, deletion, search, and status tracking.

---

## 🏗️ Application Architecture

This project follows the **MVC (Model-View-Controller)** pattern:

| Layer | Technology |
|-------|------------|
| **Model** | MySQL Database via SQLAlchemy ORM |
| **View** | HTML5 + CSS3 + Jinja2 Templates |
| **Controller** | Flask Routes (`app.py`) |

> **Development Approach:** Code-First using SQLAlchemy — database tables are auto-generated from Python models.

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Backend** | Python 3.10, Flask, Flask-SQLAlchemy |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Database** | MySQL |
| **Auth** | Session-based, Werkzeug Password Hashing |
| **Version Control** | Git & GitHub |

---

## ✨ Features

### 👤 User Features
- ✅ Register & Login
- ✅ Secure password hashing (Werkzeug)
- ✅ Create, View, Edit, Delete tasks
- ✅ Search tasks
- ✅ Status tracking (Pending / Completed)
- ✅ Due date management
- ✅ Auto timestamps on creation & update
- ✅ Created By & Updated By tracking

### 👑 Admin Features
- ✅ View & manage all users
- ✅ Edit & delete any user
- ✅ View & manage all tasks
- ✅ Edit & delete any task
- ✅ Role-based access control (Admin / User)

---

## 📊 Task Attributes

| Attribute | Description |
|-----------|-------------|
| `title` | Task name |
| `description` | Task details |
| `due_date` | Deadline |
| `status` | Pending / Completed |
| `remarks` | Additional notes |
| `created_on` | Creation timestamp |
| `updated_on` | Last updated timestamp |
| `created_by` | Creator user ID (FK) |
| `updated_by` | Last updater user ID (FK) |

---

## 🗄️ Database Design

### ER Diagram

The system uses a relational design where one user can create multiple tasks, linked via foreign keys.

![ER Diagram](./er-diagram.png)

### Data Dictionary

#### `users` Table

| Column | Data Type | Description |
|--------|-----------|-------------|
| `id` | INT (PK, AUTO_INCREMENT) | Unique user identifier |
| `name` | VARCHAR(100) | Full name |
| `email` | VARCHAR(100) | Email address |
| `password` | VARCHAR(255) | Hashed password |
| `role` | VARCHAR(20) | Role — Admin or User |

#### `tasks` Table

| Column | Data Type | Description |
|--------|-----------|-------------|
| `id` | INT (PK, AUTO_INCREMENT) | Unique task identifier |
| `title` | VARCHAR(255) | Task title |
| `description` | TEXT | Task description |
| `due_date` | DATE | Task deadline |
| `status` | VARCHAR(50) | Task status |
| `remarks` | TEXT | Additional notes |
| `created_on` | DATETIME | Creation timestamp |
| `updated_on` | DATETIME | Last update timestamp |
| `created_by` | INT (FK → users.id) | Creator reference |
| `updated_by` | INT (FK → users.id) | Last modifier reference |

### Index Documentation

| Index | Column(s) | Purpose |
|-------|-----------|---------|
| Primary Key | `id` | Unique row identification |
| Foreign Key | `created_by`, `updated_by` | User relationship lookups |
| Search Index | `title`, `status` | Optimized filtering & search |

---

## 🔐 Authentication & Security

- Session-based authentication with Flask
- Password hashing via Werkzeug
- Protected routes — unauthenticated users redirected to login
- Role-based authorization: Admin sees all data, Users see only their own

---

## 📁 Project Structure

```
task-manager/
│
├── app.py                  # Flask app & route definitions
├── models.py               # SQLAlchemy models (User, Task)
├── extensions.py           # Flask extensions (DB, login manager)
├── requirements.txt        # Python dependencies
├── er-diagram.png          # ER diagram image
├── README.md
│
├── templates/
│   ├── index.html          # Task list (user view)
│   ├── add.html            # Add task form
│   ├── edit.html           # Edit task form
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── admin.html          # Admin dashboard
│   └── edit_user.html      # Edit user form (admin)
│
└── static/
    └── style.css           # Global styles (Glass UI)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Run this in your MySQL client:

```sql
CREATE DATABASE taskdb;
```

Then update your connection string in `app.py` or `extensions.py`:

```python
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://username:password@localhost/taskdb"
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```
http://127.0.0.1:5000
```

---

## 🔄 API Endpoints

| Operation | Endpoint | Method | Access |
|-----------|----------|--------|--------|
| View all tasks | `/` | GET | User |
| Add a task | `/add` | POST | User |
| Edit a task | `/edit/<id>` | POST | User / Admin |
| Delete a task | `/delete/<id>` | GET | User / Admin |
| Search tasks | `/search` | POST | User |
| Admin dashboard | `/admin` | GET | Admin only |
| Edit a user | `/edit_user/<id>` | POST | Admin only |
| Delete a user | `/delete_user/<id>` | GET | Admin only |

---

## 🎨 UI Highlights

- Glassmorphism design aesthetic
- Clean dashboard layout
- Responsive tables and forms
- Action buttons with smooth interaction

---

## 👨‍💻 Developer Credits

### 🚀 Project Lead & Developer

**Nishchal Dagar**    
- 📧 Email: nishchal083@gmail.com
---

## ⭐ Support

If you found this project useful, consider giving it a **star** on GitHub — it means a lot!
Thank You
