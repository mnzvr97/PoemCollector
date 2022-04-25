import imp
from tkinter import EW
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import poem, Author
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IsReadForm
from django.views.generic import ListView, DetailView

class poemCreate(CreateView):
    model = poem
    fields = ['name', 'published', 'image']
    def form_valid(self, form):
        form.instance.user = 1
        #self.request.user
        return super().form_valid(form)
    # success_url = "/poems/"
class poemUpdate(UpdateView):
    model = poem
    fields = ['author', 'name', 'image']
class poemDelete(DeleteView):
    model = poem
    success_url = '/poems/'

    
# ]
# Create your views here.
def home(request):
    #using django method from library called http, httpresponse which is just like res.send from express - sends to browswer
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def poems_index(request):
    poems = poem.objects.all()
    return render(request, 'poems/index.html', {'poems': poems})

def poem_details(request, poem_id):
    poem = poem.objects.get(id=poem_id)
    authors_poem_doesnt_have = poem.objects.exclude(id_in = poem.author.all()).values_list('id')
    read_form = IsReadForm()
    return render(request, 'poems/detail.html', {'poem': poem, 'readform': read_form, 'author': authors_poem_doesnt_have})

def add_read(request, poem_id):
    form = IsReadForm(request.POST)
    if form.is_valid():
        new_read = form.save(commit=False)
        new_read.poem_id = poem_id
        new_read.save()
    return redirect('detail', poem_id = poem_id)

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'poems']

class AuthorDelete(DeleteView):
    model = Author
    success_url = '/authors/'

def assoc_author(request, poem_id, author_id):
    poem.objects.get(id=poem_id).author.add(author_id)
    return redirect('detail', poem_id = poem_id)

def unassoc_author(request, poem_id, author_id):
    poem.objects.get(id=poem_id).author.remove(author_id)
    return redirect('detail', poem_id = poem_id)

