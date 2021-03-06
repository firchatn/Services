from django.shortcuts import render
from .models import Service, Worker



# Create your views here.
def index(request):
    service = Service.objects.all()
    return render(request,'job/index.html', {'service' : service})


# View service onClick on img service new page render with filter service
# 2 optinel param city of woker on status (libre,oucuper)
def one_service(request, city=None, status=None):
    service = request.GET.get('service')
    workers = Worker.objects.all()
    return render(request,'job/finder.html',{'workers' : workers, 'service' : service})

def profile(request):
    idprofil = request.GET.get('profil')
    worker = Worker.objects.get(id=idprofil)
    return render(request, 'job/profile.html', {'worker' : worker})