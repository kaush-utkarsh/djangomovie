from django.urls import path
from .  import views

urlpatterns = [
    path('',views.childView, name ="childView" ),
    path('register/',views.signupView, name ="signupView" ),
    path('login/',views.loginView, name ="loginView" ),
    path('logout/',views.logoutView, name ="logoutView" ),
    path('base/',views.baseView, name ="baseView" ),
    path('addCountry/',views.countryFormView, name ="countryFormView" ),
    path('addMovie/',views.movieFormView, name ="movieFormView" ),
    path('viewMovie/',views.movieListView, name ="movieListView" ),
    path('viewMovies/',views.moviesView, name ="moviesView" ),
]
