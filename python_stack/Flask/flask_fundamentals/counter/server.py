from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
app.count = 0

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html', count=session['count'])


@app.route('/destroy_session', methods = ["POST"])
def reset():
    session['count'] = 0	
    return redirect('/')


@app.route('/add', methods = ["POST"])
def add_tow():
    session['count'] += 2 -	1
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)  