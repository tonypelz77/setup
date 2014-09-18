from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from options.forms import UserForm

def index(request):
	context = RequestContext(request)
	context_dict = {'message':"Hello Pelz Options"}
	return render_to_response('options/index.html', context_dict, context)
	
def about(request):
	context = RequestContext(request)
	context_dict = {'aboutmessage' : "I am About"}
	return render_to_response('options/about.html', context_dict, context)
	
def contact(request):
	context = RequestContext(request)
	context_dict = {'message' : "no message"}
	return render_to_response('options/contact.html', context_dict, context)
	
def otkf(request):
	context = RequestContext(request)
	context_dict = {'message' : "no message"}
	return render_to_response('options/otkf.html', context_dict, context)
	
def bth(request):
	context = RequestContext(request)
	context_dict = {'aboutmessage' : "I am About"}
	return render_to_response('options/bth.html', context_dict, context)
	
def chimera(request):
	context = RequestContext(request)
	context_dict = {'aboutmessage' : "I am About"}
	return render_to_response('options/chimera.html', context_dict, context)

def email(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			#user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()
	return render_to_response(
		'options/email.html',
		{'user_form': user_form, 'registered': registered},
		context)