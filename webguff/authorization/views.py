from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login(request):
	print ("Hello WebGuff")
	print (request)
	#return "Hello World"
	print request.POST.get('game')
	return HttpResponse("Hello WebGuff10")
