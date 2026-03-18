<h1 align="center">🚀 Task Management System</h1>
<p align="center">A modern full-stack web application to manage your daily tasks — built with Flask, MySQL, and a clean Glass UI.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-red?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-Design-blue?style=for-the-badge&logo=css3&logoColor=white" />
</p>

---

## 📌 Overview

**Task Management System** is a full-stack web application that helps you organize and track your tasks efficiently. It supports creating, viewing, editing, deleting, and searching tasks — all with proper timestamp tracking and status management.

---

## 🏗️ Architecture

This project follows the **MVC (Model-View-Controller)** pattern:

| Layer | Technology |
|-------|------------|
| **Model** | MySQL Database |
| **View** | HTML5 + CSS3 + Jinja2 Templates |
| **Controller** | Flask Routes (`app.py`) |

---

## 🛠️ Tech Stack

**Backend**
- Python 3.10
- Flask

**Frontend**
- HTML5
- CSS3
- Jinja2 Templates

**Database**
- MySQL

**Version Control**
- Git & GitHub

---

## ✨ Features

- ✅ Add new tasks
- ✅ View all tasks
- ✅ Edit existing tasks
- ✅ Delete tasks
- ✅ Search tasks by keyword
- ✅ Due date tracking
- ✅ Status management (Pending / Completed)
- ✅ Auto timestamps for creation and updates
- ✅ Track who created or last updated a task

---

## 📊 Task Attributes

| Attribute | Description |
|-----------|-------------|
| `title` | Task name |
| `description` | Detailed description of the task |
| `due_date` | Deadline for the task |
| `status` | Current status — Pending or Completed |
| `remarks` | Any additional notes |
| `created_on` | Timestamp of creation |
| `updated_on` | Timestamp of last update |
| `created_by` | Name of the user who created the task |
| `updated_by` | Name of the user who last modified the task |

---

## 🗄️ Database Schema

### `tasks` Table

| Column | Data Type | Description |
|--------|-----------|-------------|
| `id` | INT (PK, AUTO_INCREMENT) | Unique task identifier |
| `title` | VARCHAR(255) | Task title |
| `description` | VARCHAR(500) | Task description |
| `due_date` | DATE | Task deadline |
| `status` | VARCHAR(50) | Task status |
| `remarks` | VARCHAR(255) | Additional notes |
| `created_on` | DATETIME | Creation timestamp |
| `updated_on` | DATETIME | Last update timestamp |
| `created_by` | VARCHAR(100) | Creator name |
| `updated_by` | VARCHAR(100) | Last modifier name |

---

## 📁 Project Structure

```
task-manager/
│
├── app.py                  # Main Flask application & routes
├── models.py               # Database models
├── extensions.py           # Flask extensions (e.g. SQLAlchemy)
├── requirements.txt        # Python dependencies
│
├── templates/
│   ├── index.html          # Task list view
│   ├── add.html            # Add task form
│   └── edit.html           # Edit task form
│
├── static/
│   └── style.css           # Application styles
│
└── README.md
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

Log into MySQL and run:

```sql
CREATE DATABASE taskdb;
```

Then update your database connection settings in `extensions.py` or wherever your config lives:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/taskdb"
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

| Operation | Endpoint | Method |
|-----------|----------|--------|
| View all tasks | `/` | GET |
| Add a task | `/add` | POST |
| Edit a task | `/edit/<id>` | POST |
| Delete a task | `/delete/<id>` | GET |
| Search tasks | `/search` | POST |

---

## 🎨 UI Highlights

- Glass-morphism design aesthetic
- Clean, minimal layout
- Responsive across screen sizes
- Interactive buttons with smooth feedback

---

## 👨‍💻 Developer

**Nishchal Dagar**  
B.Tech CSE — Data Science

---

## ⭐ Support

If you found this project helpful, consider giving it a star on GitHub — it helps a lot!