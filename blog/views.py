from django.shortcuts import get_object_or_404, render
from . models import Blog

# Create your views here.

def showBlogs(request):
    blog=Blog.objects
    return render (request, 'blog/showBlog.html', {'blogs':blog})

def detalle(request, blogs_id):
    det_blog=get_object_or_404(Blog, pk=blogs_id)
    return render(request, 'blog/detalle.html',{'blog':det_blog})
 