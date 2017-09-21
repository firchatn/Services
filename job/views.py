from django.shortcuts import render
from .models import Service, Worker



# Create your views here.
def index(request):
    service = Service.objects.all()
    return render(request,'job/index.html', {'service' : service})


# View service onClick on img service new page render with filter service
# 2 optinel param city of woker on status (libre,oucuper)
def one_service(request, service, city=None, status=None):
    oneService = Worker.objects.filter(work=service)
    return render(request,'job/finder.html',{'oneservice' : oneService})
