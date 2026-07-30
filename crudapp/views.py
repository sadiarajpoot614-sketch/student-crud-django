from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def index(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    students = Student.objects.all()

    context = {
        'form': form,
        'students': students
    }

    return render(request, 'index.html', context)


def edit(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)

    students = Student.objects.all()

    context = {
        'form': form,
        'students': students
    }

    return render(request, 'index.html', context)


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')