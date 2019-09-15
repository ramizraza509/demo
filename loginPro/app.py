from flask import Flask,render_template,request,sessions,logging,url_for,redirect
#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_sessionmaker

#from passlib.hash import _sha256

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)
