from django.shortcuts import render
from . models import Job

# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detalle(request, blogs_id):
    det_blog=get_object_or_404(Blog, pk=blogs_id)
    return render(request, 'jobs/detalle.html',{'blog':det_blog})