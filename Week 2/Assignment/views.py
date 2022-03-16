#add this file in the same directory where urls.py is located
from django.http import HttpResponse

def home(request):
	# add your individual unique string into the response
    return HttpResponse("Hello, world. Week 0200a913 is the polls index.") 
