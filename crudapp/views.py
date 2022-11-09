from django.shortcuts import render, HttpResponseRedirect
from .models import Employee

def HomePage(request):
    data = Employee.objects.all()
    return render(request, "index.html", {"data":data})

## Adding new student.
def AddNew(request):
    if (request.method == 'POST'):
        rcd = Employee()
        rcd.name = request.POST.get("name")
        rcd.des = request.POST.get("des")
        rcd.phone = request.POST.get("phone")
        rcd.email = request.POST.get("email")
        rcd.city = request.POST.get("city")
        rcd.state = request.POST.get("state")
        rcd.save()
        return HttpResponseRedirect("/")
    return render(request, "add.html")

def DeleteRcd(request, id):
    dt = Employee.objects.get(ID=id)
    dt.delete()
    return HttpResponseRedirect("/")

def UpdateRcd(request, id):
    dt = Employee.objects.get(ID=id)
    if(request.method=="POST"):
        dt.name = request.POST.get("name")
        dt.des = request.POST.get("des")
        dt.phone = request.POST.get("phone")
        dt.email = request.POST.get("email")
        dt.city = request.POST.get("city")
        dt.state = request.POST.get("state")
        dt.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html", {"dt":dt})