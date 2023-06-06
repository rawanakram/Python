from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def Time_and_Date(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime()),
    }
    return render(request, 'index.html', context)

