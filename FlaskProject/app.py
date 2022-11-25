import mysql.connector 
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['PORT'] = '3306'
app.config['MYSQL_DB'] = 'test'


mysql = MySQL(app)


# connection = mysql.connector.connect(
#     user="root", password="aniket1996", host="127.0.0.1:3308", port="3308", database="test")




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        fname = details['fname']
        lname = details['lname']
        cur = mysql.connection.cursor()
        # cur=connection.cursor()
        cur.execute("INSERT INTO record(fname, lname) VALUES (%s, %s)", (fname, lname))
        mysql.connection.commit()
        cur.close()
        return 'The Data is successfully added into Record.'
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0')