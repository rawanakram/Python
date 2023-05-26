from flask import Flask, render_template, request, redirect, session
import random 
from datetime import datetime

#######################################################################
# creat a simple game to collect mony from different sources by using # 
# flask with python                                                   #
#######################################################################


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
        
    if "list" not in session:
        session["list"] = []
        session["gold"]=0
        session['count'] = 0
    gold = session["gold"]
    comments = session["list"]
    counter = session['count']
    return render_template('index.html', gold = gold, comments = comments, counter = counter)


@app.route('/process_money', methods=["post"])
def process_money():
    buldingType = request.form['building']

    if buldingType == "farm":
        amount = random.randint(10,20) 
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        comment = f"Earned {amount} golds from the {buldingType}! ({now})"
    elif buldingType == "cave":
        amount = random.randint(5,10)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        comment = f"Earned {amount} golds from the {buldingType}! ({now})" 
    elif buldingType == "house":
        amount = random.randint(2,5)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        comment = f"Earned {amount} golds from the {buldingType}! ({now})"
    else:
        amount = random.randint(-50,50)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        if amount>0:
            comment = f"Earned {amount} golds from the {buldingType}! ({now})"
        else:
            comment = f"Entered the {buldingType} and lost {abs(amount)} golds... Ouch.. ({now})"    
   
    session['gold'] += amount
    session['count'] += 1
    session["list"].insert(0,comment)
    print(f"you have  {session['gold']}")
    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)