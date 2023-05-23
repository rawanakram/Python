from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    count = strawberry + raspberry + apple
    now=datetime.now() 
    print(request.form)
    print(f"Charging { first_name } { last_name } for { count } fruit") 
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, apple=apple,
                           first_name=first_name, last_name=last_name, student_id=student_id, count=count, now=now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)  