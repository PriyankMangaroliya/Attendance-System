from flask import Flask, render_template
from config import init_db_connection

app = Flask(__name__)

# Initialize MongoDB from config.py
init_db_connection(app)

@app.route('/')
def home():
    return 'Attendance System'

@app.route("/login")
def login():
    return render_template("auth-login.html")

if __name__ == '__main__':
    app.run(debug=True)