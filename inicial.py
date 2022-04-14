from flask import Flask, render_template, request, jsonify


app = Flask(__name__,template_folder='templates')


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def homepage():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)