from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members,Watched,Wishlist,Favorite,Searched
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from CinemaAtoZ import settings

def index(request):
  mymembers=Members.objects.all().values()
  template = loader.get_template('index.html')
  context={
    'mymembers':mymembers
  }
  return HttpResponse(template.render(context,request))

def watched(request):
  mywatched=Watched.objects.all().values()
  template= loader.get_template('watched.html')
  context={
    'mywatched':mywatched
  }
  return HttpResponse(template.render(context,request))

def favourites(request):
  myfav=Favorite.objects.all().values()
  template= loader.get_template('favourites.html')
  context={
    'myfav':myfav
  }
  return HttpResponse(template.render(context,request))

def wishlist(request):
  mywish=Wishlist.objects.all().values()
  template= loader.get_template('wishlist.html')
  context={
    'mywish':mywish
  }
  return HttpResponse(template.render(context,request))

def watch(request,id):
  """for adding a movie to watchlist

  Args:
      id (int): id of the movie in Members database

  Returns:
      HTML : redirects to the homepage
  """
  m=Members.objects.get(id=id)
  wa=Watched(ido=m.ido,User=User.objects.get(username=request.user.username),Title=m.Title,Rating=m.Rating,Year=m.Year,IMDb_Rating=m.IMDb_Rating,Rott_Rating=m.Rott_Rating,Meta_Rating=m.Meta_Rating,Cast=m.Cast,Genre=m.Genre,Duration=m.Duration,Plot=m.Plot,similar=m.similar,review=m.review)
  wa.save()
  return HttpResponseRedirect(reverse('index'))

def wish(request,id):
  """for adding a movie to wishlist

  Args:
      id (int): id of the movie in Members database

  Returns:
      HTML : redirects to the homepage
  """
  m=Members.objects.get(id=id)
  wi=Wishlist(ido=m.ido,User=User.objects.get(username=request.user.username),Title=m.Title,Rating=m.Rating,Year=m.Year,IMDb_Rating=m.IMDb_Rating,Rott_Rating=m.Rott_Rating,Meta_Rating=m.Meta_Rating,Cast=m.Cast,Genre=m.Genre,Duration=m.Duration,Plot=m.Plot,similar=m.similar,review=m.review)
  wi.save()
  return HttpResponseRedirect(reverse('index'))

def like(request,id):
  """for adding a movie to favourites

  Args:
      id (int): id of the movie in Members database

  Returns:
      HTML : redirects to the homepage
  """
  m=Members.objects.get(id=id)
  li=Favorite(ido=m.ido,User=User.objects.get(username=request.user.username),Title=m.Title,Rating=m.Rating,Year=m.Year,IMDb_Rating=m.IMDb_Rating,Rott_Rating=m.Rott_Rating,Meta_Rating=m.Meta_Rating,Cast=m.Cast,Genre=m.Genre,Duration=m.Duration,Plot=m.Plot,similar=m.similar,review=m.review)
  li.save()
  return HttpResponseRedirect(reverse('index'))

def dele(request,id):
  """deleting a movie from wishlist

  Args:
      id (int): id of the movie in Wishlist database

  Returns:
      HTML : redirects to the wishlist page
  """
  m=Wishlist.objects.get(id=id)
  m.delete()
  return HttpResponseRedirect(reverse('wishlist'))

def watch1(request,id):
  """for adding a movie to watchlist

  Args:
      id (int): id of the movie in Wishlist database

  Returns:
      HTML : redirects to the wishlist page
  """
  m=Wishlist.objects.get(id=id)
  wa=Watched(ido=m.ido,User=User.objects.get(username=request.user.username),Title=m.Title,Rating=m.Rating,Year=m.Year,IMDb_Rating=m.IMDb_Rating,Rott_Rating=m.Rott_Rating,Meta_Rating=m.Meta_Rating,Cast=m.Cast,Genre=m.Genre,Duration=m.Duration,Plot=m.Plot,similar=m.similar,review=m.review)
  wa.save()
  return HttpResponseRedirect(reverse('wishlist'))

def like1(request,id):
  """for adding a movie to favourites

  Args:
      id (int): id of the movie in Wishlist database

  Returns:
      HTML : redirects to the wishlist page
  """
  m=Wishlist.objects.get(id=id)
  li=Favorite(ido=m.ido,User=User.objects.get(username=request.user.username),Title=m.Title,Rating=m.Rating,Year=m.Year,IMDb_Rating=m.IMDb_Rating,Rott_Rating=m.Rott_Rating,Meta_Rating=m.Meta_Rating,Cast=m.Cast,Genre=m.Genre,Duration=m.Duration,Plot=m.Plot,similar=m.similar,review=m.review)
  li.save()
  return HttpResponseRedirect(reverse('wishlist'))

def dele2(request,id):
  """deleting a movie from watched movies

  Args:
      id (int): id of the movie in Watched database

  Returns:
      HTML : redirects to the watched page
  """
  m=Watched.objects.get(id=id)
  m.delete()
  return HttpResponseRedirect(reverse('watched'))

def like2(request,id):
  """for adding a movie to favourites

  Args:
      id (int): id of the movie in Watched database

  Returns:
      HTML : redirects to the watched page
  """
  m=Watched.objects.get(id=id)
  li=Favorite(ido=m.ido,User=User.objects.get(username=request.user.username),Title=m.Title,Rating=m.Rating,Year=m.Year,IMDb_Rating=m.IMDb_Rating,Rott_Rating=m.Rott_Rating,Meta_Rating=m.Meta_Rating,Cast=m.Cast,Genre=m.Genre,Duration=m.Duration,Plot=m.Plot,similar=m.similar,review=m.review)
  li.save()
  return HttpResponseRedirect(reverse('watched'))

def deletef(request,id):
  """deleting a movie from Favourite movies

  Args:
      id (int): id of the movie in Favorite database

  Returns:
      HTML : redirects to the homepage
  """
  Favorite.objects.get(id=id).delete()
  return HttpResponseRedirect(reverse('index'))

def search(request):
  """search bar process

  Args: 

  Returns:
      HTML: shows a page containing the search results
  """
  for x in Searched.objects.all():
    x.delete()
  name=request.POST['sea']
  for each in Members.objects.all():
    if each.Title==name:
      li=Searched(ido=each.ido,Title=each.Title,Rating=each.Rating,Year=each.Year,IMDb_Rating=each.IMDb_Rating,Rott_Rating=each.Rott_Rating,Meta_Rating=each.Meta_Rating,Cast=each.Cast,Genre=each.Genre,Duration=each.Duration,Plot=each.Plot,similar=each.similar,review=each.review)
      li.save()
  mysearch=Searched.objects.all().values()
  template = loader.get_template('search.html')
  context={
    'mysearch':mysearch
  }
  return HttpResponse(template.render(context,request))

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            global fname
            fname=user.first_name
            return render(request, "index.html", {'fname':fname})
        else:
            messages.error(request, "Bad credintials! Invalid username or password")
            return redirect('index')

    return render(request, "signin.html")

def signout(request):

    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! please try someother username")
            return redirect('index')
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('index')
        if len(username)>10:
            messages.error(request, "Username must be within 10 characters")
        if password1 != password2:
            messages.error(request, "Passwords didn't match")
        if not username.isalnum():
            messages.error(request, "Username should contain either alphabets or numericals")
            return redirect('index')



        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")


        return redirect('signin')
    return render(request, "signup.html")