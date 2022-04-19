from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='templates')

app.config['MYSQL_HOST'] = 'to_do_list_mysql_1'
app.config['MYSQL_USER'] = 'jessica'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'LALA'
 
mysql = MySQL(app)


@app.route('/', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/home')
def homepage():
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO tabela VALUES("a")''')
    mysql.connection.commit()
    cursor.close()
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)