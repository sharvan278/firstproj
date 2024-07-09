from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sharvan@2005",
    database="grocTrack"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('index'))
        else:
            return "Invalid email or password!"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form.get('phone', '')

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            return "User already exists!"
        else:
            cursor.execute("INSERT INTO users (name, email, password, phone) VALUES (%s, %s, %s, %s)", (name, email, password, phone))
            db.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/baby_care')
def baby_care():
    return render_template('baby_care.html')

@app.route('/beauty')
def beauty():
    return render_template('beauty.html')

@app.route('/best_deals')
def best_deals():
    return render_template('best_deals.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact_form')
def contact_form():
    return render_template('contact_form.html')

@app.route('/feedback_confirm')
def feedback_confirm():
    return render_template('feedback_confirm.html')

@app.route('/feedback_form', methods=['GET', 'POST'])
def feedback_form():
    if request.method == 'POST':
        # Handle feedback form submission
        return redirect(url_for('feedback_confirm'))
    return render_template('feedback_form.html')

if __name__ == '__main__':
    app.run(debug=True)
