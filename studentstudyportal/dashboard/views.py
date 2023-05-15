from django.shortcuts import redirect, render
from .forms import *
from django.core.checks import messages
from django.contrib import messages
from django.views import generic


# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')
def notes(request):
    if request.method =="POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username}successfully")  
    else:
      form = NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")
class NotesDetailView(generic.DetailView):
    model=Notes

def homework(request):
    form=Homeworform()
    homework=Homework.objects.filter(user=request.user)
    if len(homework)==0:
        homework_done =True
    else:
        homework_done=False    
    context={'homeworks':homework,'homeworks_done':homework_done,'form':form}
    return render(request,'dashboard/homework.html',context) 
def todo(request):
    if request.method =='POST':
        form= TodoForm(request.POST)
        if form.is_valid():
            try:
                finished =request.POST["is_finished"]
                if finished== 'on':
                   finished = True
                else:
                    finished= False
            except:
                finished=False           
            todos=Todo(
            user=request.user,
            title=request.POST['title'],
            is_finished=finished
           ) 
            todos.save()
            messages.success(request,f"Todo added from {request.user.username}!!")
    else:
        form=TodoForm()        
    todo=Todo.objects.filter(user=request.user)
    if len(todo)==0:
        todos_done=True
    else:
         todos_done=False    
    context={
        'form':form,
        'todos':todo,
        'todos_done':todos_done
    }
    return render(request,"dashboard/todo.html",context)

def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
       todo.is_finished= False
    else:
        todo.is_finished=True
    todo.save()
    return redirect('todo')  

def delete_todo(request,pk=None): 
    Todo.objects.get(id=pk).delete() 
    return redirect("todo")  
def books(request):
    return render(request,"dashboard/books.html")


