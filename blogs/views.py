from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import  Blog, category

# Create your views here.


def posts_by_category(request, category_id):
     
    posts = Blog.objects.filter(status='published', category_id = category_id)
    Category = category.objects.get(id=category_id)
    Category = get_object_or_404(category, pk=category_id)
    context = {

        ' posts': posts,

        'Category': Category, 
    }
   
    return render(request,'posts_by_category.html', context)