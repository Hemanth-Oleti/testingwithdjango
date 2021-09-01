from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Population(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    population = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.city) + " - "+ str(self.population)

