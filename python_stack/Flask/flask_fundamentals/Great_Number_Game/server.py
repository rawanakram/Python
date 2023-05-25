
from flask import Flask, render_template, request, redirect, session
import random 


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if "random" not in session:
        session["random"] = random.randint(1,100)
    if  'guess' not in session:
        session['guess'] = 0
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    print(session["random"])
    return render_template('index.html', num = session['random'], guessNum= session['guess'], count=session['count'])


@app.route('/guess', methods = ["POST"])
def guess():
    session['guess'] = int(request.form['answer'])
    return redirect('/')


@app.route('/reset', methods = ["POST"])
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True) 
