from django.shortcuts import render
from .models import Person
from .forms import empForm
from django.http import HttpResponse
from django.views.generic.edit import UpdateView 
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect)
# Create your views here.
def create_view(request):
    context={}
    
    form=empForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('Person has been added!')
    context['form']=form

    return render(request,"employees/create_view.html",context)
    
def list_view(request): 
    context ={} 
  
    context["dataset"] = Person.objects.all() 
          
    return render(request, "employees/list_view.html", context)     
    
    
# pass id attribute from urls 
def detail_view(request, id): 
    context ={} 
  
    context["data"] = Person.objects.get(id = id) 
          
    return render(request, "employees/detail_view.html", context)     
    
def update_view(request, id): 
    context ={} 
  
    obj = get_object_or_404(Person, id = id) 
  
    # pass the object as instance in form 
    form = empForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "employees/update_view.html", context) 
    
def delete_view(request, id): 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Person, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
  
    return render(request, "employees/delete_view.html", context)     
    
def home(request):
    return render(request,"employees/home.html",{'name':'Poonam'})
    
def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    res=int(val1)+int(val2)
    return render(request,"employees/result.html",{'result':res})