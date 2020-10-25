from .models import *

def stringReplace(txtvar=''):
	newtxtvar = txtvar.replace('a','@')
	return newtxtvar

def sendCountries():
	dictvalues = []
	dictvalues.append({'value':'IN','countryname':'India'})
	dictvalues.append({'value':'US','countryname':'United States'})
	dictvalues.append({'value':'CN','countryname':'China'})
	dictvalues.append({'value':'ZA','countryname':'South Africa'})
	dictvalues.append({'value':'RU','countryname':'Russia'})
	return dictvalues


def addNewCountry(formdata = None):
	Countries.objects.create(countryname=formdata['countryname'])
	return True

def getAllCountries():
	data = Countries.objects.all()
	return data


def fetchOneCountry(id=''):
	data = Countries.objects.get(pk=id)
	return data

def editCountry(formdata = None):
	country = Countries.objects.get(pk=formdata['countryid'])
	country.countryname = formdata['countryname']
	country.save()
	return True

def addNewMovie(formdata = None):
	movie = Actionmovies(moviename=formdata['moviename'])
	movie.description = formdata['desc']
	movie.countryid = Countries.objects.get(pk=formdata['countryid'])
	movie.save()
	return True

def getAllMovies():
	data = Actionmovies.objects.all()
	return data

def fetchOneMovie(id=''):
	data = Actionmovies.objects.get(pk=id)
	return data

def editMovie(formdata = None):
	movie = Actionmovies.objects.get(pk=formdata['movieid'])
	movie.moviename = formdata['moviename']
	movie.countryid = Countries.objects.get(pk=formdata['countryid'])
	movie.description = formdata['desc']
	movie.save()
	return True