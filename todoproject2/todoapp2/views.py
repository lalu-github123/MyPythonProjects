from django.shortcuts import render,redirect
from .models import TodoModel
from .forms import update_form

# Create your views here.

def home(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=TodoModel(name=name,priority=priority,date=date)
        task.save()
    show=TodoModel.objects.all()
    return render(request,"home.html",{'show':show})
def update(request,id):
    task=TodoModel.objects.get(id=id)
    f=update_form(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        redirect('/')
    return render(request,"update.html",{'f':f,'task':task})
def delete(request,id):
    task=TodoModel.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

