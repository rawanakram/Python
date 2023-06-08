from django.shortcuts import render, redirect 
import random 


# Create your views here.
def root(request):
    if 'random' not in request.session:
        request.session['random'] = random.randint(1,100)
    if 'guess' not in request.session:
        request.session['guess'] = 0
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] +=1
    print(request.session['guess'])
    print(request.session['random'])
    print(request.session['counter'])
    context = {
        'randomNum':request.session['random'],
        'guessNum':request.session['guess'],
        'count': request.session['counter'],
    }
    return render(request, 'index.html', context)


def guess_method(request):
    request.session['guess'] = int(request.POST['answer'])
    return redirect ('/')


def reset(request):
    del request.session['guess']
    del request.session['random']
    del request.session['counter']
    return redirect ('/')