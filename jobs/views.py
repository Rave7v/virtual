from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings 
from django.core.mail import send_mail

import jobs
from . models import Job

# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})



def detallej(request, jobs_id):
    det_job=get_object_or_404(Job, pk=jobs_id)
    return render(request, 'jobs/detallej.html',{'jobs':det_job})


def enviarcorreo(request):
    if request.method=="POST":
        subject=request.POST['asunto']
        message=request.POST['mensaje']+"     |    Remitente: "+ request.POST['correo']+"     |    Producto: "+ request.POST['productos']
      
        


        email_from= settings.EMAIL_HOST_USER

        recipent_list=["aldairldrago99@gmail.com"]  
        send_mail(subject, message, email_from, recipent_list)
        return redirect('enviarcorreo')

    return render (request, "solicitud.html") 
        
