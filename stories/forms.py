from django import forms
from .models import Story
# Creates a form for users to submit their stories.
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description', 'category', 'author_name', 'email', 'media_url']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


# title = models.CharField(max_length=200)
#     description = models.TextField()
#     category = models.CharField(max_length=100, choices=[     
#                     ('Motivational', 'Motivational'),
#                     ('Heartbreaking', 'Heartbreaking'),
#                     ('Exciting', 'Exciting'),
#                     ('Interesting', 'Interesting'),
#                     ('Horror', 'Horror')
#         ])
    
#     author_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     media_url = models.URLField(blank = True, null = True)
#     timestamp = models.DateTimeField(auto_now_add=True)