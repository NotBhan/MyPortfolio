from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.

def homepage(request):
    # context = {
    #     'name' : ['Chandrabhan', 'Suresh', 'Ramesh'],
    #     'age' : [25, 30, 35],
        
    # }
    # name = ['Chandrabhan', 'Suresh', 'Ramesh']
    # age = [25, 30, 35]
    # context = zip(name, age)
    data = {
    'fruits' : ['apple', 'banana', 'orange'],
        
    }
    return render(request, 'myapp/index.html', data)

def hello_view(request):
    # return render(request, 'myapp/index.html')
    xyz = Student.objects.all()  # Fetch all Student objects from the database
    context = {
        'students': xyz,  # Pass the fetched
    }
    return render(request, 'myapp/hello.html', context)

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # save to DB
            return render(request, 'myapp/index.html')  # or redirect
    else:
        form = StudentForm()
    
    return render(request, 'myapp/student_form.html', {'form': form})