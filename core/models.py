from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    live_url = models.URLField()
    github_url = models.URLField()
    image = models.ImageField(upload_to='projects/')

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    icon = models.ImageField(upload_to='skills/')

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    text = models.TextField()
    photo_url = models.URLField()