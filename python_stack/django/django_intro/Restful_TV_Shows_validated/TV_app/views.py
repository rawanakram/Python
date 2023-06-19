from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show


# Create your views here.
def showAll(request):
    all_shows = Show.objects.all()

    context = {
        'all_shows':all_shows,
    }
    return render(request, 'show_all.html', context)


def newshow(request):
    return render(request, 'new_show.html')


def creatshow(request):

    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    
        return redirect('/shows/new')

    else:
        show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        desc = request.POST['desc'],
        release_date = request.POST['releasedate']
        )
        show_id = show.id
        messages.success(request, "Show successfully added")
        return redirect('/shows/' + str(show_id))



def showdetails(request, show_id):
    show = Show.objects.get(id = int(show_id))
    all_shows = Show.objects.all()
    context = {
        'show':show,
        'all_shows':all_shows
    }
    return render(request, 'show_details.html', context)


def editshow(request, show_id):
    all_shows = Show.objects.all()
    show = Show.objects.get(id = int(show_id))

    context = {
        'show':show,
        'all_shows':all_shows
    }
    return render(request, 'update_show.html', context)


def updateshow(request, show_id):

    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(F'/shows/{show_id}/edit')

    else:
        show_to_update = Show.objects.get(id = int(show_id))
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.desc = request.POST['desc']
        show_to_update.release_date = request.POST['releasedate']
        show_to_update.save()
        
        return redirect('/shows/' + str(show_id))

        
def deleteshow(request, show_id):
    show_to_delete = Show.objects.get(id = int(show_id))
    show_to_delete.delete()
    return redirect('/shows')