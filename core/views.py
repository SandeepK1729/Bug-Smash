from django.shortcuts import render, redirect, HttpResponse

from .forms import ParticipantRegistrationForm, QuestionForm, participantsVerificationForm, TestCreationForm

from .models import User, Question, Test

from django.contrib.auth.decorators import login_required
from .decorators import admin_login_required

from .helper import getFormattedData

@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form_data = {key: val for key, val in request.POST.items()}
        form_data['password'] = request.POST.get('username', '')
        form_data['is_active'] = False

        form = ParticipantRegistrationForm(
                    form_data,
                    request.FILES,
                )
        
        if form.is_valid():
            form.save()
            return HttpResponse("Registered Successfully")
    else:
        form = ParticipantRegistrationForm()
    
    return render(request, 'form.html', {
        'form' : form,
        'title' : 'Registration Form',
        'data_type' : 'file',
        'form_type' : 'register'
    })

@admin_login_required
def view_participants(request):
    participants = User.objects.filter(is_staff = False)
    headers = ['username', 'first_name', 'last_name', 'is_active', 'mobile_number', 'email', 'college_name', 'department', 'year', 'transaction_id']
    
    return render(request, 'table.html', {
        'title' : "Participants",
        'headers' : [
                        " ".join([x.capitalize() for x in header.split('_')])  for header in headers
                    ],
        'model_keys' : headers,
        'data' : getFormattedData(participants, headers),
    })

@admin_login_required
def participantsVerification(request):
    if request.method == "POST":
        transaction_ids     = request.POST.get("enter_list_of_transaction_ids")
        unverified_participants = User.objects.filter(is_active = False)

        for participant in unverified_participants:
            if participant.transaction_id in transaction_ids:
                participant.is_active = True
                participant.save()
        
        return redirect('participants')
    
    else:
        form = participantsVerificationForm()

    return render(request, 'form.html', {
        'form' : form,
        'title' : 'Participants Verification Form',
        'form_type' : 'verify'
    })

@admin_login_required
def upload_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("add question")
    
    else:
        form = QuestionForm()

    return render(request, 'form.html', {
        'form' : form,
        'title' : "Question Addition Form",
        'data_type' : 'file',
        'form_type' : 'Add Question'
    })  

@admin_login_required
def view_questions(request):
    headers = ['question_name', 'question_type', 'all_options', 'correct_options']
    questions = Question.objects.all()

    return render(request, 'table.html', {
        'title' : 'Questions',
        'headers' : [
                        " ".join([x.capitalize() for x in header.split('_')])  for header in headers
                    ],
        'model_keys' : headers, 
        'data' : getFormattedData(questions, headers)
    })
    
@admin_login_required
def create_test(request):
    if request.method == "POST":
        form = TestCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("add test")
    
    else:
        form = TestCreationForm()

    return render(request, 'form.html', {
        'form' : form,
        'title' : "Test Creation Form",
        'data_type' : 'text',
        'form_type' : 'Create Test'
    })  

@admin_login_required
def view_tests(request):
    headers = ['test_name', 'start_time', 'end_time']
    questions = Test.objects.all()

    return render(request, 'table.html', {
        'title' : 'Questions',
        'headers' : [
                        " ".join([x.capitalize() for x in header.split('_')])  for header in headers
                    ],
        'model_keys' : headers, 
        'data' : getFormattedData(questions, headers)
    })

@login_required
def participateInTest(request, test_name):
    test    = Test.objects.first(test_name = test_name)
    return test
