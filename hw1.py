from flask import Flask
from flask import render_template,request

hw1 = Flask(__name__)

@hw1.route("/",methods=["GET","POST"])
def HWagenda():
    return(render_template("HWagenda.html"))

@hw1.route("/HWq1", methods=["GET", "POST"])
def HWq1():
    return render_template("HWq1.html")

@hw1.route("/HWq2", methods=["GET", "POST"])
def HWq2():
    return render_template("HWq2.html")

@hw1.route("/HWq3", methods=["GET", "POST"])
def HWq3():
    return render_template("HWq3.html")

@hw1.route("/HWq4", methods=["GET", "POST"])
def HWq4():
    return render_template("HWq4.html")

@hw1.route("/HWq5", methods=["GET", "POST"])
def HWq5():
    return render_template("HWq5.html")

if __name__ == "__main__":
    hw1.run()
