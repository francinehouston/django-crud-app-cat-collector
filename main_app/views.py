from django.shortcuts import render, redirect
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat
# import the FeedingForm
from .forms import FeedingForm

# Create your views here.
# main_app/views.py


# Import HttpResponse to send text-based responses
from django.http import HttpResponse
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
        
# Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
  
    
class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
  
        
# Define the home view function
def home(request):
    # Send a simple HTML response
   return render(request, 'home.html') # Render the home.html template

def about(request):
    return render(request, 'about.html') # Render the about.html template

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


# update this view function
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        # include the cat and feeding_form in the context
        'cat': cat, 'feeding_form': feeding_form
    })


def cat_create(request):
      return HttpResponse("<h1>Create a Cat Form Goes Here</h1>")# Send a simple response after creation


def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)
