from flask import Flask, render_template, redirect, url_for, session, request
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
app.secret_key = 'theUltimateSecretKeyIsNothingButTheSecretItself'

db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_pass']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

usernames = []
types = [[
    {
         'type': 'Cup Cake',
         'img': '1.jpg',
         'details': 'adfadfadfdafdfad'
         },
    {
        'type': 'Donut',
        'img': '2.jpg',
        'details': 'lklkjakldsflkdfkladlk'
    },
    {
        'type': 'Cake Slices',
        'img': '3.jpg',
        'details': 'adfadfadfdafdfad'
    },
    {
        'type': 'Cup Cake',
        'img': '1.jpg',
        'details': 'adfadfadfdafdfad'
    },
    {
        'type': 'Donut',
        'img': '2.jpg',
        'details': 'lklkjakldsflkdfkladlk'
    },
    {
        'type': 'Cake Slices',
        'img': '3.jpg',
        'details': 'adfadfadfdafdfad'
    }
]]


def is_logged_in(sess):
    cur = mysql.connection.cursor()
    users = []
    count = cur.execute('SELECT user FROM users')
    if count > 0:
        for i in cur.fetchall():
            users.append(i[0])
    cur.close()
    print('is_logged_in(): Users: ',users)
    if sess:
        if sess['user'] in users:
            return True
    else:
        return False


@app.route('/')
def home():
    if is_logged_in(session):
        print(session['user'])
        return render_template('index.html', is_logged_in=True, items=types)
    return render_template('index.html', items=types)


@app.route('/signup', methods=['POST'])
def signup():
    print('#####/signup#####')
    user = request.form['user']
    email = request.form['email']
    password = request.form['password']
    print(user,email,sha256_crypt.hash(password))

    # Store creds in DB
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(user,email,password) VALUES(%s,%s,%s);",(user,email,sha256_crypt.hash(password)))
    print('Inserted into Table...')
    mysql.connection.commit()
    cur.close()
    print('Comitted...')
    
    # Store Session values
    session['user'] = user
    print('Session Set')
    return render_template('index.html', is_logged_in = True, items=types)


@app.route('/signin',methods=['POST'])
def signin():
    print('#####/signin#####')
    user = request.form['user']
    password = request.form['password']
    print(user,sha256_crypt.hash(password))

    # Verify creds
    cur = mysql.connection.cursor()
    count = cur.execute("SELECT user,password FROM users WHERE user=%s;",[user])
    if count > 0:
        username,hashed_pass = cur.fetchone()
        print(username,hashed_pass)
        print(sha256_crypt.verify(password,hashed_pass))
        if sha256_crypt.verify(password,hashed_pass):
            print('Verified')
            session['user'] = username
            print('Session Set')
            return render_template('index.html', is_logged_in=True, items=types)
    return render_template('index.html', log_in_error=True, items=types)


@app.route('/signout')
def signout():
    session.pop('user')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)