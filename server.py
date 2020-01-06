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


@app.route('/')
def home():
    return render_template('index.html', items=types)


@app.route('/signup', methods=['POST'])
def signup():
    print('adfad')
    if request.method == 'POST':
      user = request.form['user']
      email = request.form['email']
      password = request.form['password']
      print(user,email,password)


if __name__ == '__main__':
    app.run(debug=True)