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
    workers = Worker.objects.filter(work=service)
    return render(request,'job/finder.html',{'workers' : workers})
