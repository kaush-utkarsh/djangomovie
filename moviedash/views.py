from django.shortcuts import render, redirect
from .commonfunctions import *
from .appdecorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

# Create your views here.


@login_required(login_url = '/login/')
def baseView(request):
	return render(request, 'base.html')

@userAuthCheck
def signupView(request):
	if request.method == 'POST':
		
		user = User.objects.filter(username=request.POST['username'])
		if user.exists():
			print("user exists")
			return render(request, 'signup.html')
		else:
			print('this is a new user')
			user = User.objects.create_user(request.POST['username'],None,request.POST['password'])
			user.first_name = request.POST['firstname']
			user.last_name = request.POST['lastname']
			user.save()
			group = Group.objects.get(name="normaluser")
			group.user_set.add(user)
			group.save()
			return redirect('/login/')	
	return render(request, 'signup.html')

@userAuthCheck
@checkUserGroup(grouplist = ['admin'])
def countryFormView(request):
	renddict ={'action': 'Add'}
def loginView(request):
	if request.method == 'POST':
		user = authenticate(username= request.POST['username'], password = request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			print('WRONG USER')
	return render(request, 'login.html')

def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect('/login/')	

# @login_required(login_url = '/login/')
def childView(request):
	renddict = {'title':'Dashboard Root'}

	return render(request, 'child.html', renddict)

@login_required(login_url = '/login/')
@checkUserGroup(grouplist = ['admin'])
def countryFormView(request):
	renddict ={'action': 'Add'}
	if request.method == 'POST':
		if request.POST['countryformtype'] == 'addeditform':
			if request.POST['countryid'] == '':
				addNewCountry(request.POST)
				renddict['msg'] = "New Country Added"
			else:
				editCountry(request.POST)
				renddict['msg'] = "Country Edited"

		else:
			countryid = request.POST['countryid']
			country = fetchOneCountry(countryid)
			renddict ['country'] = country
			renddict['action'] = 'Edit'


	countrylist = getAllCountries()
	renddict['countrylist'] = countrylist

	return render(request, 'countryform.html',renddict)

@login_required(login_url = '/login/')
@checkUserGroup(grouplist = ['admin'])
def movieFormView(request):
	renddict ={'action': 'Add'}
	if request.method == 'POST':
		if request.POST['movieid'] == '':
			addNewMovie(request.POST)
			renddict['msg'] = "New Movie Added"
		else:
			editMovie(request.POST)
			renddict['msg'] = "Country Edited"

	countrylist = getAllCountries()
	renddict['countrylist'] = countrylist

	return render(request, 'movieform.html',renddict)

@login_required(login_url = '/login/')
@checkUserGroup(grouplist = ['admin'])
def movieListView(request):
	renddict ={'title': 'Movie List'}
	if request.method == 'POST':
		movieid = request.POST['movieid']
		movie = fetchOneMovie(movieid)
		renddict ['movie'] = movie
		renddict['action'] = 'Edit'
		countrylist = getAllCountries()
		renddict['countrylist'] = countrylist
		return render(request, 'movieform.html',renddict)


	movielist = getAllMovies()
	renddict['movielist'] = movielist

	return render(request, 'movielist.html',renddict)



@login_required(login_url = '/login/')
@checkUserGroup(grouplist = ['admin','normaluser'])
def moviesView(request):
	renddict ={'title': 'Movie List'}
	movielist = getAllMovies()
	renddict['movielist'] = movielist
	return render(request, 'movies.html',renddict)
