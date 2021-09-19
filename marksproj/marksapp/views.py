from django.shortcuts import render
from marksapp.models import marks
from marksapp.forms import marksform
# Create your views here.

def marks_view(request):
    return render(request,'marks.html')

def marks1_view(request):
    form=marksform()
    if request.method=='POST':
        form=marksform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return marks_view(request)
    return render(request,'marks1.html',{'form':form})

def marks2_view(request):
    marks_list=marks.objects.all()
    return render(request,'marks2.html',{'marks_list':marks_list})
