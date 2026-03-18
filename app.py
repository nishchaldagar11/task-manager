from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Jaat%40123dagar@localhost/taskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import Task


# HOME
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


# ADD TASK
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':

        new_task = Task(
            title=request.form['title'],
            description=request.form['description'],
            due_date=request.form['due_date'],   # NEW
            status=request.form['status'],
            remarks=request.form['remarks'],
            created_by=request.form['created_by']
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html')


# EDIT TASK
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.due_date = request.form['due_date']   # NEW
        task.status = request.form['status']
        task.remarks = request.form['remarks']
        task.updated_by = request.form['updated_by']
        task.updated_on = datetime.utcnow()        # NEW

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)


# DELETE
@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


# SEARCH
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    tasks = Task.query.filter(Task.title.contains(keyword)).all()
    return render_template('index.html', tasks=tasks)


# RUN
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)