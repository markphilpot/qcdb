from django.template import Context, loader
from django.http import HttpResponse

from qcdb.web.models import Comic
from qcdb.web.models import Character
from qcdb.web.models import Location
from qcdb.web.models import Event
from qcdb.web.models import Dialog

def index(request):
    latest_comics = Comic.objects.all().order_by('-num')[:5]
    t = loader.get_template('templates/index.html')
    c = Context({
        'latest_comics': latest_comics,
        })

    return HttpResponse(t.render(c))

def comic(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    t = loader.get_template('templates/comic.html')
    c = Context({
                 'comic': comic,
                 })
    
    return HttpResponse(t.render(c))

def comics(request):
    comics = Comic.objects.all().order_by('-num')
    t = loader.get_template('templates/comics.html')
    c = Context({
                 'comics': comics,
                 })
    
    return HttpResponse(t.render(c))

def characters(request):
    characters = Character.objects.all().order_by('name')
    t = loader.get_template('templates/characters.html')
    c = Context({
                 'characters': characters,
                 })
    
    return HttpResponse(t.render(c))
    
def character(request, character_id):
    character = Character.objects.get(id=character_id)
    t = loader.get_template('templates/character.html')
    c = Context({
                 'character': character,
                 })
    
    return HttpResponse(t.render(c))

def locations(request):
    locations = Location.objects.all()
    t = loader.get_template('templates/locations.html')
    c = Context({
                 'locations': locations,
                 })
    
    return HttpResponse(t.render(c))

def location(request, location_id):
    location = Location.objects.get(id=location_id)
    t = loader.get_template('templates/location.html')
    c = Context({
                 'location': location,
                 })
    
    return HttpResponse(t.render(c))

def events(request):
    events = Event.objects.all()
    t = loader.get_template('templates/events.html')
    c = Context({
                 'events': events,
                 })
    
    return HttpResponse(t.render(c))

def search(request):
    searchString = request.POST['search_box']
    
    import sphinxsearch
    
    client = sphinxsearch.SphinxClient()
    client.SetServer('localhost', 3312)
    
    result = client.Query(searchString)
    
    comicDict = {}
    
    for match in result['matches']:
        dialog = Dialog.objects.get(id=match['id'])
        comic = dialog.comic.all()[0]
        
        # Make sure the search string is present
        # this will happen if the match is the title
        # perfomance penalty... fix later.
        import re
        
        if not re.compile( searchString ).search(dialog.text):
            if comicDict.has_key(comic):
                continue
        
        if comicDict.has_key(comic):
            comicDict[comic].append(dialog)
        else:
            comicDict[comic] = [dialog]
    
    t = loader.get_template('templates/search.html')
    c = Context({
                 'comicDict': comicDict,
                 'searchString': searchString,
                 })
    
    return HttpResponse(t.render(c))
    
    
    