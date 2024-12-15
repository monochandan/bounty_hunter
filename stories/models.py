from django.db import models
# Defines the data structure for storing story information in the database.
# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[     
                    ('Motivational', 'Motivational'),
                    ('Heartbreaking', 'Heartbreaking'),
                    ('Exciting', 'Exciting'),
                    ('Interesting', 'Interesting'),
                    ('Horror', 'Horror')
        ])
    
    author_name = models.CharField(max_length=100)
    email = models.EmailField()
    media_url = models.URLField(blank = True, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
