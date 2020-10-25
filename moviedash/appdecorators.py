from django.shortcuts import render, redirect
from django.http import HttpResponse


def userAuthCheck(viewMeth):
	def chlidFunc(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')	
		else:
			return viewMeth(request, *args, **kwargs)
	return chlidFunc

def checkUserGroup(grouplist = []):
	def decorator(viewMeth):
		def childFunc(request, *args, **kwargs):
			if request.user.groups.exists():
				groups = request.user.groups.all()
				for group in groups:
					if group.name in grouplist:
						return viewMeth(request,*args,**kwargs)
			return HttpResponse("You dont have access rights for this page. Contact Site Owners.")
		return childFunc
	return decorator
