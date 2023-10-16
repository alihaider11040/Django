
# Create your views here.
from django.shortcuts import render, redirect
from .models import Class, Student, Subject

def home(request):
    if request.method == 'POST':
        # Get the selected class and year
        class_id = request.POST['class']
        year = request.POST['year']

        # Retrieve students and subjects for the selected class
        selected_class = Class.objects.get(pk=class_id)
        students = Student.objects.filter(enrolled_class=selected_class)
        subjects = selected_class.grade.subjects.all()

        # You can create a form for entering and saving marks here

        return render(request, 'marksheet.html', {'students': students, 'subjects': subjects})

    classes = Class.objects.all()
    return render(request, 'home.html', {'classes': classes})

def save_marks(request):
    # Handle saving marks to the database
    return

def confirm_and_send_results(request):
    return
    # Handle confirmation and sending results to parents
def send_results():
    return

