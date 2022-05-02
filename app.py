from ast import Delete
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


def create_new_user(email, password):
    cursor = mysql.connection.cursor()
    sql = 'INSERT INTO User (email, password) VALUES (%s, %s)'
    logger.error(f'Criando log de erro {email}, {password}')
    data_user = (email, password)
    cursor.execute(sql, data_user)
    mysql.connection.commit()
    cursor.close()


def find_user_in_database(email, password):
    cursor = mysql.connection.cursor()
    sql = f"SELECT email FROM LALA.User WHERE email = '{email}' AND password = '{password}'"
    cursor.execute(sql) 
    data = cursor.fetchall()
    logger.info(f'criando log de info {data}')
    cursor.close()
    if data:
        return True
    return False


def redirect_user_to_home_id(user_email, user_password):
    cursor = mysql.connection.cursor()
    sql = f"SELECT id_user FROM User WHERE email = '{user_email}' AND password = '{user_password}'"
    cursor.execute(sql) 
    data = cursor.fetchall()
    id_data = data[0]
    cursor.close()
    return redirect(f'home/{id_data[0]}')


def add_new_task(id_user):
    cursor = mysql.connection.cursor()
    user_task = request.form['user-task']
    dead_line = request.form['dead-line']
    date_creation = datetime.now()
    sql = 'INSERT INTO Tasks (user_task, dead_line, date_creation, id_user) VALUES (%s, %s, %s,%s)'
    data_task = (user_task, dead_line, date_creation, id_user )
    cursor.execute(sql, data_task)
    mysql.connection.commit()
    cursor.close()

def delete_task():
    cursor = mysql.connection.cursor()
    id_task_delete = request.form['submit']
    sql = f'DELETE FROM Tasks WHERE id_tasks = "{id_task_delete}"'
    cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()


@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        user_email = request.form['email-user']
        user_password = request.form['user-password']
        email_validation(user_email)
        password_validation(user_password)

        if find_user_in_database(user_email, user_password) == False:
            return redirect('register')
        else:
            return redirect_user_to_home_id(user_email, user_password)            

    return render_template("login.html")


@app.route('/home/<id_user>', methods = ['POST', 'GET'])
def homepage(id_user):
    cursor = mysql.connection.cursor()
   
    if request.method == "POST":
        if request.form['submit'] == 'cadastrar':
            add_new_task(id_user)
        elif request.form['submit'] == 'edit':
            logger.error(f'CCCCCCCCCC')
        else:
            delete_task()
  
    sql = f"select * from Tasks WHERE id_user = {id_user}"
    cursor.execute(sql) 
    data = cursor.fetchall() #data from database
    cursor.close()
    
    return render_template("homepage.html",value=data, id=id_user)
    

@app.route('/register', methods = ['POST', 'GET'])
def register():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        register_user_email = request.form['register-email-user']
        register_user_password = request.form['register-user-password']

        email_validation(register_user_email)
        password_validation(register_user_password)
        
        sql = f"SELECT email FROM User WHERE email = '{register_user_email}'"
        cursor.execute(sql) 
        data = cursor.fetchall()

        if data:
            logger.error(f'{register_user_email} já cadastrado')
            raise ValueError(f'{register_user_email} já cadastrado')
      
        create_new_user(register_user_email, register_user_password)
        redirect_user_to_home_id(register_user_email, register_user_password)
        
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)