from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def index(request):
    all_todo_items=TodoItem.objects.all()
    return render(request,'todo_app/index.html',{'all_items':all_todo_items})

def addTodo(request):
    new_item=TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    itemDelete=TodoItem.objects.get(id=todo_id)
    itemDelete.delete()
    return HttpResponseRedirect('/todo/')

def home(request):
    return HttpResponseRedirect('/todo/')
  
