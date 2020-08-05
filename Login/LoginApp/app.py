from typing import List, Dict
import simplejson as json
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_mail import Mail, Message

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'LoginData'
mysql.init_app(app)

app.config['SECRET_KEY'] = 'WebApp'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_DEFAULT_SENDER'] = 'njitprojectis601@gmail.com'
mail = Mail(app)

name = ''


@app.route('/', methods=['GET'])
def homepage():
    return render_template('login.html', title='Login Page')


@app.route('/profile', methods=['GET'])
def profile():
    if name:
        user = {'Username': name}
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM Accounts')
        return render_template('profile.html', title='User Profile', user=user)
    else:
        return redirect(url_for("login"))


@app.route('/login', methods=['POST'])
def login():
    inputData = (request.form.get('Email'), request.form.get('Password'))
    cursor = mysql.get_db().cursor()
    query = """SELECT * FROM Accounts WHERE Email = %s AND Password = %s"""
    cursor.execute(query, inputData)
    result = cursor.fetchall()
    count = cursor.rowcount

    if count == 0:
        return render_template('login.html', title='Login Page', response='Incorrect Email and/or Password.')
    else:
        if result[0]['verified'] == 1:
            global name
            name = result[0]['First Name'] + ' ' + result[0]['Last Name']
            return redirect('/profile', code=302)
        else:
            return render_template('login.html', title='Login Page', response='Please check your email'
                                                                              ' to verify account.')


@app.route('/register')
def register_page():
    return render_template('register.html', title='Register')


@app.route('/register', methods=['POST'])
def register():
    inputData = (request.form.get('First_Name'), request.form.get('Last_Name'), request.form.get('Email'),
                 request.form.get('Password'))
    email = request.form.get('Email')

    cursor = mysql.get_db().cursor()
    email_check_query = """SELECT id FROM Accounts where Email = %s"""
    new_input_query = """INSERT INTO Accounts (First_Name, Last_Name, Email, Password, Verified) VALUES (%s, %s, %s, %s, 
    0)"""
    cursor.execute(email_check_query, email)
    email_exist = cursor.rowcount

    if email_exist == 1:
        return render_template('register.html', title='Register', response='An account with this email already exists. '
                                                                           'Please login.')
    else:
        cursor.execute(new_input_query, inputData)
        mysql.get_db().commit()
        cursor.execute(email_check_query, email)
        result = cursor.fetchall()

        msg = Message('Please verify your account', recipients=[email])
        msg.body = ('Please click here to activate you account. '
                    'You will be able to log in once your account has been activated.')
        msg.html = (f'<h1>Verify Account</h1>'
                    f'<p>Please '
                    f'<a href=\"http://0.0.0.0:5000/activate/{result[0]["id"]}\">click here</a> to activate your '
                    f'account.</p><br><i>You will be able to log in once your account has been activated.</i>')
        mail.send(msg)
        return render_template('register.html', title='Register', response_s=f'Success! Please check email ({email}) '
                                                                             f'for link to verify your account.')


@app.route('/activate/<int:new_id>', methods=['GET'])
def activate(new_id):
    cursor = mysql.get_db().cursor()
    sql_update_query = """UPDATE Accounts a SET a.verified = 1 WHERE a.id = %s"""
    cursor.execute(sql_update_query, new_id)
    mysql.get_db().commit()
    return render_template('index.html', title='Login',
                           status='Your account has been successfully verified.  Please login.')


@app.route('/accounts', methods=['GET'])
def accounts():
    user = {'username': 'Kelly'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Accounts')
    result = cursor.fetchall()
    return render_template('accounts.html', title='Accounts', user=user, Accounts=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
