#WSGI=web server gateway interface
from flask import Flask,render_template,request

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
if __name__=="__main__":
    app.run(port="9000",host="localhost",debug=True)