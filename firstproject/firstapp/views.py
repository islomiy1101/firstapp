from django.shortcuts import render
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>Welcome to my first Django Page</h1>')

def about(r):
    return HttpResponse("<h1 style='color:red;text-transform:uppercase'>This is another Django Views</h1>")    

def index(request):
    str='I am from views file'
    data=['red','green','blue','magenta']
    context={'colors':data,'string':str}
    return render(request,'index.html',context)