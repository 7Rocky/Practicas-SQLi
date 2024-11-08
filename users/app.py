import sqlite3

from flask import Flask, g, redirect, render_template, request
from hashlib import sha256


app = Flask(__name__)
DATABASE = 'users.db'


def get_db():
    if getattr(g, '_database', None) is None:
        g._database = sqlite3.connect(DATABASE)

    return g._database


def init_db(ddl: str):
    with app.app_context():
        db = get_db()

        with open(ddl) as sql:
            db.executescript(sql.read())

        db.commit()


@app.route('/', methods=['GET'])
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login() -> tuple[str, int]:
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        if not username or not password:
            return render_template('login.html', error='Blank username or password.'), 400

        db = get_db()
        cursor = db.cursor()
        hashed_password = sha256(password.encode()).hexdigest()

        try:
            cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{hashed_password}'")
        except:
            return render_template('login.html', error='Login failed. Invalid username or password.'), 400

        if cursor.fetchone():
            return render_template('login.html', success='Welcome! You are now logged in.'), 200

        return render_template('login.html', error='Login failed. Invalid username or password.'), 400

    return render_template('login.html'), 200


@app.route('/register', methods=['GET', 'POST'])
def register() -> tuple[str, int]:
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm-password', '')

        if not username or not password:
            return render_template('register.html', error='Blank username or password.'), 400

        if password != confirm_password:
            return render_template('register.html', error='Password and confirm password do not match.'), 400

        db = get_db()
        cursor = db.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', (username, ))

        if cursor.fetchone():
            return render_template('register.html', error='Registration failed. User already exists.'), 400

        hashed_password = sha256(password.encode()).hexdigest()

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        db.commit()

        return render_template('register.html', success='User registered correctly.'), 200

    return render_template('register.html'), 200


@app.teardown_appcontext
def close_connection(exception):
    if (db := getattr(g, '_database', None)) is not None:
        db.close()


if __name__ == '__main__':
    init_db('users.sql')
    app.run(host='0.0.0.0', debug=False, port=4000)
