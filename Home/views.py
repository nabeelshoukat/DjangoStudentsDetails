from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import students
# Create your views here.
def index(request):
    if request.method=='POST':
        fname=request.POST.get('first name')
        lname=request.POST.get('last name')

        dt=students(first_name=fname,last_name=lname)
        dt.save()
        return HttpResponse("data has been saved")
    return render(request,'index.html')
    # return HttpResponse("this is a text")

