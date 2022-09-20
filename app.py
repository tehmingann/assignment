from flask import Flask, render_template, request, redirect, url_for, flash
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'
 
app = Flask(__name__)
app.secret_key = "qZdNHdse/IMs2JY9+AnIO4ksMbC3E++rEDCLUULI"
  
   
db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'
 
@app.route('/')
def Index():
    
    cur = db_conn.cursor()
 
    cur.execute('SELECT * FROM employee')
    data = cur.fetchall()
  
    cur.close()
    return render_template('index.html', employee = data)
 
@app.route('/add_contact', methods=['POST'])
def add_employee():
    
    cur = db_conn.cursor()
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur.execute("INSERT INTO employee (name, email, phone) VALUES (%s,%s,%s)", (fullname, email, phone))
        conn.commit()
        flash('Employee Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    
    cur = db_conn.cursor()
  
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', employee = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_employee(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE employee
            SET name = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Employee Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_employee(id):
    
    cur = db_conn.cursor()
  
    cur.execute('DELETE FROM employee WHERE id = {0}'.format(id))
    conn.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('Index'))
 
# starting the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
