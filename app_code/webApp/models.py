from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Authors model
#Authors can login, logout, create stories, post stories and get stories
class Authors(models.Model):
    author_username = models.ForeignKey(User, on_delete = models.CASCADE)
    author_name = models.CharField (max_length=100)

    def __str__(self):
        return self.author_username.username 

class NewsStories(models.Model):
    story_id = models.AutoField(primary_key=True) #Auto incrementing
    #headline of the story    
    story_headline = models.CharField(max_length=64)
    #stories author
    story_author = models.ForeignKey(Authors, on_delete = models.CASCADE) #foreign key to the authors table
    #date story was posted
    story_date = models.DateField(max_length=100)
    #possible choices for Category
    categoryChoices =[
        ('pol', 'Politics'),
        ('art','Art News'),
        ('tech','Technology News'),
        ('trivia','Trivial News')
    ]
    story_cat = models.CharField(max_length=10, choices = categoryChoices)

    #Possible choices for the region the story is about 
    regionChoices =[
        ('uk','UK'),
        ('eu','European News'),
        ('w','World News'), 
        ]
    story_region = models.CharField(max_length=10,choices = regionChoices)
    #main text of the story
    story_details = models.CharField(max_length=512)    
    
    		
