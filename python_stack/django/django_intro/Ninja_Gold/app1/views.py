from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def root(request):
    if 'list' not in request.session:
        request.session['list'] = []
        request.session['count'] = 0
        request.session['gold'] = 0
    conext = {
        'gold': request.session['gold'],
        'comments':request.session["list"],
        'counter':int(request.session['count']),
    }
    return render(request, 'index.html', conext)


def process_money(request):
    buldingType = request.POST['building']

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

    request.session['gold'] += amount
    request.session['count'] += 1
    request.session["list"].insert(0,comment)
    request.session.save()
    print(f"you have  {request.session['gold']}")
    return redirect('/')


def reset(request):
    del request.session['gold']
    del request.session['count']
    del request.session['list']
    return redirect('/')
