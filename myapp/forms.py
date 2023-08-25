from ftplib import MAXLINE
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label= "nombre la tarea", max_length="500")
    
    description= forms.CharField(widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label= "nombre del proyecto", max_length="500")
