from django.shortcuts import render

def game_index(request):
	template = loader.get_template('polls/index.html')
	return HttpResponseRedirect(template.render(request))
