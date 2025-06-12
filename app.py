#WSGI=web server gateway interface
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/nawa",methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        return f"hello, {name}"
    return render_template("posting.html")
    

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"hello, {name}"
    return render_template("posting.html")

@app.route("/number/<int:num>")
def number(num):
    return "the number given is " +str(num)

@app.route("/result/<int:score>")
def result(score):
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("result.html",results=res)

@app.route("/tutu",methods=["POST","GET"])
def tutu():
    total_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        math=float(request.form["math"])
        c=float(request.form["C"])
        date_science=float(request.form["data science"])
        
        total_score=(science+c+date_science+math)/4
    else:
        return render_template("score.html")
    return redirect(url_for("result",score=total_score))
        

if __name__=="__main__":
    app.run(port="9000",host="localhost",debug=True)