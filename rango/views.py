from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {	'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!",
						'testmessage': "This is my first message which I am going to pass to a template. =)"	}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier. # Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {	'aboutmessage': "This tutorial has been put together by Nicola Mossner.",
						'catmessage': "I am a cat."	}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier. # Note that the first parameter is the template we wish to use.
	return render(request, 'rango/about.html', context=context_dict)
