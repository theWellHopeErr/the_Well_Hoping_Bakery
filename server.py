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

users = []
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
    }
],
    [
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
], ]


# def isloggedin(sess):
#     if sess:
#         cur = mysql.connection.cursor()
#         cur_count = cur.execute('SELECT user FROM users;')
#         if cur_count > 0:
#             usernames = cur.fetchall()
#         if sess['user'] in usernames:
#             return True
#     else:
#         return False


@app.route('/')
def home():
    return render_template('index.html', items=types)


@app.route('/signup', methods=['GET'])
def signup():
    print('adfad')
    if request.method == 'GET':
      user = request.form['user']
      email = request.form['email']
      password = request.form['password']
      print(user,email,password)


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/purchase')
# def purchase():
#     # print('session', session)
#     if session:
#         usernames.append([i['user'] for i in users])
#         # print('usernames', usernames)
#         if [session['user']] in usernames:
#             # print([session['user']] in usernames)
#             return render_template('modal.html', showModal=True)
#     return redirect(url_for('signUpPage'))


# @app.route('/signup')
# def signUpPage():
#     if session:
#         usernames.append([i['user'] for i in users])
#         if [session['user']] in usernames:
#             return render_template('index.html', items=types, loggedIn=True)
#     return render_template('auth.html', showAuth=False)


# @app.route('/signup', methods=['POST'])
# def signUp():
#     if request.method == 'POST':
#         print('user: ', request.json)
#         user = request.json['user']
#         email = request.json['email']
#         password = request.json['password']
#         session['user'] = user
#         session['email'] = email
#         session['password'] = sha256_crypt.hash(password)
#         users.append({
#             'user': user,
#             'email': email,
#             'password': password
#         })
#         print('Users: ', users)
#     return redirect(url_for('purchase'))


# @app.route('/log', methods=['POST'])
# def log():
#     if session:
#         usernames.append([i['user'] for i in users])
#         if [session['user']] in usernames:
#             session.clear()
#             return redirect(url_for(home))
#     else:
#         return redirect(url_for(purchase))
