from django.http import HttpResponse
from django.template import loader

def index(request):
     template = loader.get_template('home/index.html')
     context = {} #TODO: ADD information about available lobbies before clicking the enter button

     return HttpResponse(template.render(context, request))
