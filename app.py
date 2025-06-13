from flask import Flask, render_template, request, redirect
from models import init_db, insert_user, get_users

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    users = get_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    if name:
        insert_user(name)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
