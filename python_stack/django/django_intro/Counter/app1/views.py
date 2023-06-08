from django.shortcuts import render, redirect

# Create your views here.
def root(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return render(request, 'index.html')


def destroy (request):
    del request.session['counter']	
    return redirect('/')


def add (request):
    request.session['counter'] +=2-1	
    return redirect('/')