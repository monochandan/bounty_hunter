from django.shortcuts import render, redirect
from .forms import StoryForm
from .models import Story
# Defines functions to handle story submission and display submitted stories.
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def submit_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            #form = StoryForm()
            #logger.error(f"Invalid form submission: {form.errors}")
            return render(request, 'stories/submit_story.html', {'form': form})
        
    else:
        form = StoryForm()
        return render(request, 'stories/submit_story.html', {'form': form})
    
    

def home(request):
    stories = Story.objects.order_by('-timestamp') #  latest story on top
    return render(request, 'stories/home.html', {'stories': stories})
