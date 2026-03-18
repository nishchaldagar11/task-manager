from flask import Flask, render_template, request, redirect, url_for, session
from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Jaat%40123dagar@localhost/taskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import User, Task


# 🔐 REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=generate_password_hash(request.form['password'])
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')


# 🔐 LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()

        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect('/')

    return render_template('login.html')


# 🔓 LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# 🏠 HOME
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')

    tasks = Task.query.filter_by(created_by=session['user_id']).all()
    return render_template('index.html', tasks=tasks)


# ➕ ADD TASK
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        new_task = Task(
            title=request.form['title'],
            description=request.form['description'],
            due_date=request.form['due_date'],
            status=request.form['status'],
            remarks=request.form['remarks'],
            created_by=session['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')

    return render_template('add.html')


# ✏ EDIT TASK
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    if 'user_id' not in session:
        return redirect('/login')

    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.due_date = request.form['due_date']
        task.status = request.form['status']
        task.remarks = request.form['remarks']
        task.updated_by = session['user_id']
        task.updated_on = datetime.utcnow()

        db.session.commit()
        return redirect('/')

    return render_template('edit.html', task=task)


# ❌ DELETE TASK
@app.route('/delete/<int:id>')
def delete_task(id):
    if 'user_id' not in session:
        return redirect('/login')

    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


# 🔍 SEARCH
@app.route('/search', methods=['POST'])
def search():
    if 'user_id' not in session:
        return redirect('/login')

    keyword = request.form['keyword']

    tasks = Task.query.filter(
        Task.title.contains(keyword),
        Task.created_by == session['user_id']
    ).all()

    return render_template('index.html', tasks=tasks)


# 👑 ADMIN DASHBOARD
@app.route('/admin')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    user = User.query.get(session['user_id'])

    if user.role != 'admin':
        return "Access Denied ❌"

    users = User.query.all()
    tasks = Task.query.all()

    return render_template('admin.html', users=users, tasks=tasks)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    if 'user_id' not in session:
        return redirect('/login')

    admin = User.query.get(session['user_id'])

    if admin.role != 'admin':
        return "Access Denied ❌"

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return redirect('/admin')


@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/login')

    admin = User.query.get(session['user_id'])

    if admin.role != 'admin':
        return "Access Denied ❌"

    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.role = request.form['role']

        db.session.commit()
        return redirect('/admin')

    return render_template('edit_user.html', user=user)


# 🚀 RUN
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)