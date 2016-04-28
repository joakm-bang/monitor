from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
#from django.template import loader

from .models import Computer
maxTime = 60*5


# Create your views here.
def activity(request):
    
    computers = Computer.objects.filter()
    #for computer in computers:
        #if (timezone.now() - computer.activity < timezone.timedelta(seconds=maxTime)):
            #computer.color = 'alive'
        #else:
            #computer.color = 'dead'
    context = {
        'computers':computers,
        }
    return render(request, 'monitor/activity.html', context)


#def index(request):
    #computer_list = Computer.objects.all()  # get all computers in table
    ##template = loader.get_template('monitor/index.html')  # go get the template in the monitor folder
    #context = {
        #'computer_list':computer_list,
        #}  #pass dictionary of arguments along with the template
    #return render(request, 'monitor/index.html', context)  # make the webpage given the request (what is it here?), template and context (arguments)

#def detail(request, computer_name):
    #computer = get_object_or_404(Computer, pk=computer_name)
    ##try:
        ##computer = Computer.objects.get(pk=computer_name)
    ##except Computer.DoesNotExist:
        ##raise Http404("Computer does not exist")
    #return render(request, 'monitor/detail.html', {'computer': computer})


#def latest(request):
    #resp = []
    #computers = Computer.objects.all()
    #for computer in computers:
        #activity = Activity.objects.get(computer_name = computer.computer_name)
        #latest = activity.objects.order_by('-activity')[0]
    #response = "The latest activity for computer %s."
    #return HttpResponse(response % computer_id)
    