from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL
import os

app=Flask(__name__)

mysql=MySQL(app)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']



@app.route('/')
def home():
    return render_template('page.html', title='Home')

@app.route('/Activities', methods=['GET', 'POST'])
def Activities():

    if request.method =='POST':
        details=request.form
        act=details['activ']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO Activity (Name) VALUES (%s);", [act]) #works in GCP SQL
        mysql.connection.commit()
        cur.close()

    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM Activity")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()

    
    info=[]

    for row in rows:
        info.append(row)
    
    return render_template("Activities.html", title='Activities', info1=info)


@app.route('/Activities/delete', methods=['GET', 'POST'])
def Activities_delete():
    if request.method == "POST":
        details=request.form
        act=details['activ']
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM Activity WHERE Name = (%s)", [act]) #works in GCP SQL
        mysql.connection.commit()
        cur.close()
    return render_template("Activities.html", title='Activities')
    # return render_template(url_for('Activities'))




@app.route('/Locations')
def Locations():
    return render_template('Locations.html', title='Locations')

@app.route('/WhatNext')
def WhatNext():
    return render_template('WhatNext.html', title='What next?')


if __name__=='__main__':
    app.run('0.0.0.0',debug=True)