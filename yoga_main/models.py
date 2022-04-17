from django.db import models


class UserDetails(models.Model):
  username = models.CharField(max_length = 25, unique = True)
  total_yoga_time = models.IntegerField()
  sessions_joined = models.IntegerField()