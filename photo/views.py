from django.shortcuts import render
from .models import Image, Category
from django.views.generic import ListView
from .forms import ImageSearchForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    photos=Image.objects.all()
    return render(request, 'photo/index.html', {'photos':photos})

class CategoryListView(ListView):
    template_name = 'photo/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat':self.kwargs['category'],
            'description':self.kwargs['category'],
            'images':Image.objects.filter(category__name=self.kwargs['category'])
        }
        return content

def category(request):
    category = Category.objects.exclude(name='Default')
    context = {
        'category':category,
    }
    return context

def image_search(request):
    form = ImageSearchForm()
    q = ''
    results =[]

    if 'q' in request.GET:
        form = ImageSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            
            results = Image.objects.filter(title__icontains=q)

    return render(request, 'photo/search.html', {'form':form, 'q':q, 'results':results})

