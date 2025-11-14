from django.db import models
from django.contrib.auth.models import User
from places.models import Place


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='details')
    liked_places = models.ManyToManyField(Place, related_name='liked_by', blank=True)

    def __str__(self):
        return self.user.username
