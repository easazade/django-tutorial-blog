from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # TextField is unlimited text
    # in below line timezone.now `now` is a function . note that we just want to pass
    # this function no execute it so we are not using it like `now()` we are just passing it like this `now`
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_posted = models.DateTimeField(auto_now_add=True) #saves datetime that cannot be modified later
    # date_updated = models.DateTimeField(auto_now=True) #updates this field automatically each time we change this object
