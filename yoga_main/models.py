from django.db import models


class UserDetails(models.Model):
  username = models.CharField(max_length = 25, unique = True)
  total_yoga_time = models.IntegerField()
  sessions_joined = models.IntegerField()
  skill_level = models.CharField(max_length = 50,)
  classes_created = models.IntegerField(default = 0)



class YogaClass(models.Model):
  name = models.CharField(max_length = 20)
  description = models.TextField(max_length = 50,)
  user = models.CharField( max_length = 5000)
  date = models.DateTimeField()
  rating = models.CharField(max_length = 50, default = "No Ratings Yet")
  tag = models.CharField(max_length = 10)
  link = models.CharField(default = 'Please wait 24 hours for your link to generate', max_length =50000)