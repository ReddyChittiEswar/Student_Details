from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, StudentForm

def student_list(request):
    #fetch all students
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students}) # send 'students' list to the page

def student_create(request):
    if request.method == 'POST':
        # posted model form using student instance
        studentForm = StudentForm(request.POST)
        # if valid form
        #   #i save
        #   #ii redirect to the list page
        #   return redirect('student_list') 
        if studentForm.is_valid():
            studentForm.save()
            return redirect('student_list') 
    else:
        # new model form 
        studentForm = StudentForm()
        
    return render(request, 'student_create.html', {'studentForm':studentForm}) # pass form to the page

def student_update(request, id):
    # get student instance from databse
    student = get_object_or_404(Student, pk = id)
    if request.method == 'POST':
        # posted model form using student instance
        studentForm = StudentForm(request.POST, instance = student)
        # if valid form
        #   # i save
        #   #ii redirect to the list page
        #   return redirect('student_list') 
        if studentForm.is_valid():
            studentForm.save()
            return redirect('person_list') 
    else:
        # new model form using student instance
        studentForm = StudentForm(instance = student)
    return render(request, 'student_update.html', {'studentForm':studentForm}) # pass form to the page        

def student_delete(request, id):
    # get student instance from databse 
    # delete the student in the db
    student = get_object_or_404(Student, pk = id)
    student.delete()
    return redirect('student_list') 