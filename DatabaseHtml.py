from flask import Flask
app = Flask (__name__)
from flask import render_template
import pymysql

class Database:
   def __init__(self):
      host = "127.0.0.1"
      user = "root"
      password = "Python@123@"
      db = "college"
      self.com=pymysql.connect(host=host, user=user, password=password, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
      self.cur=self.con.cursor()

      def list_students(self):
         self.cur.excecute("SELECT roll_no, name, Department FROM student");
         result= self.cur.fetchall()
         return result
@app.route("/mydb")
def mydb():
   def db_query():
      db = Database()
      stud=db.list_students()
      return stud
   res = db_query()
   #print(res)
   return render_template('student.html',result=res,content_type='application/json')
   
@app.route("/")
def hello():
   return"Hello Shatdhruka "

@app.route("/newpage")
def newfunc(mytext="guvi"):
   return render_template("jelly_bean.html", name = mytext)

if __name__ =='__main__':
   app.run(debug= True)
   
