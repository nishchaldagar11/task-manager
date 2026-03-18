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
</p>

---

## 📌 Project Overview

Task Management System is a **Full Stack Web Application** designed to manage and track tasks efficiently.

It allows users to perform full CRUD operations with proper tracking of task status, timestamps, and ownership.

---

## 🏗️ Application Architecture

This project follows **MVC Architecture**:

| Layer | Description |
|------|------------|
| Model | MySQL Database |
| View | HTML + CSS + Jinja Templates |
| Controller | Flask (app.py routes) |

---

## ⚙️ Development Approach

This project follows a **Code-First Approach** using SQLAlchemy where database tables are generated from Python models.

---

## 🎨 Frontend Structure

- Server-side rendered UI using Jinja2 templates
- Styled using custom CSS (Glass UI Design)
- Simple and responsive layout

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python
- Flask

### 🔹 Frontend
- HTML5
- CSS3
- Jinja2 Templates

### 🔹 Database
- MySQL

### 🔹 Version Control
- Git & GitHub

---

## ✨ Features

- ✅ Add Task
- ✅ View Tasks
- ✅ Edit Task
- ✅ Delete Task
- ✅ Search Task
- ✅ Status Tracking
- ✅ Due Date Management
- ✅ Auto Timestamp (Created & Updated)
- ✅ Created By & Updated By Tracking

---

## 📊 Task Attributes

| Attribute | Description |
|-----------|------------|
| title | Task name |
| description | Task details |
| due_date | Deadline |
| status | Pending / Completed |
| remarks | Notes |
| created_on | Creation timestamp |
| updated_on | Last updated timestamp |
| created_by | Creator name |
| updated_by | Last updater name |

---

## 🗄️ Database Design

### 📌 ER Diagram

> Upload your ER diagram image in repo and link below

![ER Diagram](./er-diagram.png)

---

## 📖 Data Dictionary

### Tasks Table

| Column | Data Type | Description |
|--------|----------|------------|
| id | INT (PK) | Unique Task ID |
| title | VARCHAR(255) | Task Title |
| description | TEXT | Task Description |
| due_date | DATE | Deadline |
| status | VARCHAR(50) | Task Status |
| remarks | TEXT | Notes |
| created_on | DATETIME | Created Time |
| updated_on | DATETIME | Updated Time |
| created_by | VARCHAR(100) | Creator |
| updated_by | VARCHAR(100) | Last Updater |

---

## ⚡ Index Documentation

- Primary Key indexing on `id`
- Search optimized on `title`
- Efficient filtering on `status`

---

## 📁 Project Structure

task-manager/ │ ├── app.py ├── models.py ├── extensions.py ├── requirements.txt ├── README.md ├── er-diagram.png │ ├── templates/ │   ├── index.html │   ├── add.html │   └── edit.html │ ├── static/ │   └── style.css

---

## 🔧 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Setup Database
CREATE DATABASE taskdb;
Update DB credentials in app.py:
mysql+mysqlconnector://username:password@localhost/taskdb

4️⃣ Run Application
python app.py

🌐 Open Browser
http://127.0.0.1:5000

🔄 CRUD Operations
Operation	Endpoint	Method
Create	/add	POST
Read	/	GET
Update	/edit/<id>	POST
Delete	/delete/<id>	GET
Search	/search	POST

🎨 UI Features
Glassmorphism UI
Clean layout
Responsive design
Simple navigation
👨‍💻 Developer
Nishchal Dagar
B.Tech CSE (Data Science)
⭐ Support
If you found this project useful, give it a ⭐ on GitHub!