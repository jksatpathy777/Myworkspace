
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
#tasks= ["wake-up", "brush", "bath"]
#tasks= []
#Stop declaring task as below
#tasks = ["foe", "bar", "baz"]
#Instead declare an empty task as below

#Now instead of declaring task as a global variable I will check is a particular task is present then don't add task else add new tax

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority =forms.IntegerField(label="Priority", max_value=10, min_value=1)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    

def add(request):
    if request.method == "POST":
        form= NewTaskForm(request.POST)   
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] +=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                       "form":form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })