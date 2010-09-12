from django.template import Context, loader
from django.http import HttpResponse

from qcdb.web.models import Comic
from qcdb.web.models import Character

def index(request):
    latest_comics = Comic.objects.all().order_by('num')[:5]
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
