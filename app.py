from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_mysqldb import MySQL
from datetime import datetime
from email_validation import email_validation
from password_validation import password_validation
import logging

logger = logging.getLogger('app')

app = Flask(__name__,template_folder='templates')

app.config['MYSQL_HOST'] = 'to_do_list_mysql_1'
app.config['MYSQL_USER'] = 'jessica'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'LALA'
 
mysql = MySQL(app)

def insert_user_data():
    cursor = mysql.connection.cursor()
    email = request.form['email-user']
    password = request.form['user-password']
    insert_user = 'INSERT INTO User (email, password) VALUES (%s, %s)'
    logger.error(f'Criando log de erro {email}, {password}')
    data_user = (email, password)
    cursor.execute(insert_user, data_user)
    mysql.connection.commit()
    cursor.close()

def find_user_in_database(email, password):
    cursor = mysql.connection.cursor()
    sql = f"SELECT email FROM LALA.User WHERE email = '{email}' AND password = '{password}'"
    cursor.execute(sql) 
    data_email = cursor.fetchall()
    logger.info(f'criando log de info {data_email}')
    cursor.close()
    if data_email:
        return True
    return False


@app.route('/', methods = ['POST', 'GET'])
def login():
    
    if request.method == "POST":
        user_email = request.form['email-user']
        user_password = request.form['user-password']
        email_validation(user_email)
        password_validation(user_password)
        if find_user_in_database(user_email, user_password) == False:
            insert_user_data()
            return redirect('home')

        
    return render_template("login.html")


@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        user_task = request.form['user-task']
        dead_line = request.form['dead-line']
        date_creation = datetime.now()

        insert_task = 'INSERT INTO Tasks (user_task, dead_line, date_creation) VALUES (%s, %s, %s)'
        data_task = (user_task, dead_line, date_creation )
        cursor.execute(insert_task, data_task)
        mysql.connection.commit()
        
    cursor.execute("select * from Tasks") 
    data = cursor.fetchall() #data from database
    cursor.close() 
    return render_template("homepage.html",value=data)
    

if __name__ == "__main__":
    app.run(debug=True)