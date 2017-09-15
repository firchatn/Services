from django.shortcuts import render




# Create your views here.
def index(request):
    return render(request,'job/index.html')


# View service onClick on img service new page render with filter service
# 2 optinel param city of woker on status (libre,oucuper)
def one_service(request, service, city=None, status=None):
    pass
