import sqlite3

from flask import Flask, g, render_template, request


app = Flask(__name__)
DATABASE = 'students.db'


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
def grades() -> str:
    name = request.args.get('name', '')

    if not name:
        return render_template('index.html')

    db = get_db()
    cursor = db.cursor()

    cursor.execute(f"SELECT name, subject, grade FROM grades WHERE name = '{name}'")
    results = cursor.fetchall()

    grades = [{'name': row[0], 'subject': row[1], 'grade': row[2]} for row in results]

    return render_template('index.html', grades=grades, name=name)


@app.teardown_appcontext
def close_connection(exception):
    if (db := getattr(g, '_database', None)) is not None:
        db.close()


if __name__ == '__main__':
    init_db('students.sql')
    app.run(debug=True, host='0.0.0.0', port=3000)
