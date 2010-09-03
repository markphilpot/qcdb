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
