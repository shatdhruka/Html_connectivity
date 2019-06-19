from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
   return"welcome %s" % name

@app.route('/login',methods = ["POST", "HEAD"])
def login():
   if request.method == "POST":
      user = request.form["nm1"]
      pwd = request.form["nm2"]
      return redirect(url_for("success",name = user,pwd=pwd))
   else:
      user = request.args.get("nm1")
      pwd = request.form["nm2"]
   if user=="shatdhruka" and pwd=="12345":
      return redirect(url_for("success",name = user,pwd=pwd))
   else:
      return "login failed"
if __name__ == "__main__":
   app.run(debug = True)
