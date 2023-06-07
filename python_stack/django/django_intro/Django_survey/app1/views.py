from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request, 'index.html')


def result(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    fav_language_from_form = request.POST['fav_language']
    comment_from_form = request.POST['comment']

    context = {
    	"name_on_template" : name_from_form,
    	"location" : location_from_form,
        "fav_language" : fav_language_from_form,
        "comment" : comment_from_form
    }
    return render(request, 'result.html', context)