from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import todo

# Create your views here.

def home(request):
    datalist=todo.objects.all()
    if request.method == "GET":
        data={
            "objects":datalist,
        }
        return render(request,"home.html",data)
    
    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]

        object = todo.objects.create(title= title,details=details)
        object.save()

        return redirect('home')



def add(request):
    
    return render(request,"add.html")

def delete(request):

    if request.method == "POST":
        idto = request.POST["idToDelete"]
        record = todo.objects.get(id = idto)
        record.delete()

        return redirect("http://127.0.0.1:8000")

