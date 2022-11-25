from django.db import models

class Members(models.Model):
  """Members Database which contains all the movies to be hosted on the webpage

  Args:
      models (SQL): models
  """
  ido=models.IntegerField(null=True)
  Title = models.CharField(max_length=255,null=True)
  Rating = models.CharField(max_length=255,null=True)
  Year=models.CharField(max_length=255,null=True)
  IMDb_Rating=models.CharField(max_length=255,null=True)
  Rott_Rating=models.CharField(max_length=255,null=True)
  Meta_Rating=models.CharField(max_length=255,null=True)
  Cast = models.CharField(max_length=255,null=True)
  Genre=models.CharField(max_length=255,null=True)
  Duration=models.CharField(max_length=255,null=True)
  Plot=models.CharField(max_length=255,null=True)
  similar=models.CharField(max_length=255,null=True)
  review=models.CharField(max_length=255,null=True)

class Watched(models.Model):
  """Members Database which contains all the movies watched by the user

  Args:
      models (SQL): models
  """
  User=models.CharField(max_length=255,null=True)
  ido=models.IntegerField(null=True)
  Title = models.CharField(max_length=255,null=True)
  Rating = models.CharField(max_length=255,null=True)
  Year=models.CharField(max_length=255,null=True)
  IMDb_Rating=models.CharField(max_length=255,null=True)
  Rott_Rating=models.CharField(max_length=255,null=True)
  Meta_Rating=models.CharField(max_length=255,null=True)
  Cast = models.CharField(max_length=255,null=True)
  Genre=models.CharField(max_length=255,null=True)
  Duration=models.CharField(max_length=255,null=True)
  Plot=models.CharField(max_length=255,null=True)
  similar=models.CharField(max_length=255,null=True)
  review=models.CharField(max_length=255,null=True)

class Wishlist(models.Model):
  """Members Database which contains all the movies to be watched by the user

  Args:
      models (SQL): models
  """
  User=models.CharField(max_length=255,null=True)
  ido=models.IntegerField(null=True)
  Title = models.CharField(max_length=255,null=True)
  Rating = models.CharField(max_length=255,null=True)
  Year=models.CharField(max_length=255,null=True)
  IMDb_Rating=models.CharField(max_length=255,null=True)
  Rott_Rating=models.CharField(max_length=255,null=True)
  Meta_Rating=models.CharField(max_length=255,null=True)
  Cast = models.CharField(max_length=255,null=True)
  Genre=models.CharField(max_length=255,null=True)
  Duration=models.CharField(max_length=255,null=True)
  Plot=models.CharField(max_length=255,null=True)
  similar=models.CharField(max_length=255,null=True)
  review=models.CharField(max_length=255,null=True)

class Favorite(models.Model):
  """Members Database which contains all the movies which are liked by the user

  Args:
      models (SQL): models
  """
  User=models.CharField(max_length=255,null=True)
  ido=models.IntegerField(null=True)
  Title = models.CharField(max_length=255,null=True)
  Rating = models.CharField(max_length=255,null=True)
  Year=models.CharField(max_length=255,null=True)
  IMDb_Rating=models.CharField(max_length=255,null=True)
  Rott_Rating=models.CharField(max_length=255,null=True)
  Meta_Rating=models.CharField(max_length=255,null=True)
  Cast = models.CharField(max_length=255,null=True)
  Genre=models.CharField(max_length=255,null=True)
  Duration=models.CharField(max_length=255,null=True)
  Plot=models.CharField(max_length=255,null=True)
  similar=models.CharField(max_length=255,null=True)
  review=models.CharField(max_length=255,null=True)

class Searched(models.Model):
  ido=models.IntegerField(null=True)
  Title = models.CharField(max_length=255,null=True)
  Rating = models.CharField(max_length=255,null=True)
  Year=models.CharField(max_length=255,null=True)
  IMDb_Rating=models.CharField(max_length=255,null=True)
  Rott_Rating=models.CharField(max_length=255,null=True)
  Meta_Rating=models.CharField(max_length=255,null=True)
  Cast = models.CharField(max_length=255,null=True)
  Genre=models.CharField(max_length=255,null=True)
  Duration=models.CharField(max_length=255,null=True)
  Plot=models.CharField(max_length=255,null=True)
  similar=models.CharField(max_length=255,null=True)
  review=models.CharField(max_length=255,null=True)