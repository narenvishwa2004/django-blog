from django. shortcuts import render

from blogs.models import  Blog


def home(request):

    
    featured_post = Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=True)
    context = {

        

        'featured_post':featured_post,

        'posts': posts,


        
    
    }
   
    
    return render(request, 'home.html', context)