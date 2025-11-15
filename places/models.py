from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name



class Place(models.Model):
    # Basic info
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='places/')
    description = models.TextField()

    # Relationships
    category = models.ManyToManyField(Category, related_name='places')

    # Details
    location = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    best_time = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)

    # Rating & Review
    rating = models.FloatField(default=0)
    review = models.TextField()

    def __str__(self):
        return self.title



class Attraction(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='attractions/')

    def __str__(self):
        return self.name
