from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Replace these with your actual DB credentials
conn = psycopg2.connect(
    dbname="student_db",
    user="postgres",
    dbname="student_db",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"

)
cur = conn.cursor()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll_no = request.form['roll_no']
    address = request.form['address']
    email = request.form['email']

    cur.execute("INSERT INTO students (name, roll_no, address, email) VALUES (%s, %s, %s, %s)",
                (name, roll_no, address, email))
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
