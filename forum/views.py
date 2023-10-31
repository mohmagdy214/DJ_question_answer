from django.shortcuts import render
from .models import Question , Answer
from .forms import AnswerForm
# Create your views here.

def question_list(request):
    search = Question.objects.all()
    questions = None
    if 'search_name' in request.GET:
        questions = request.GET['search_name']
        if questions:
            search = search.filter(question__icontains=questions)

    return render(request, 'forum/question_list', {'questions':search})



def question_detail(request,question_id):
    question = Question.objects.get(id=question_id)
    search2 = Answer.objects.filter(question=question)
    answers = None
    if 'search_name2' in request.GET:
        answers = request.GET['search_name2']
        if answers:
            search2 = search2.filter(answer__icontains=answers)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.question = question
            myform.save()
    else:
        form = AnswerForm()


    return render(request, 'forum/question_detail', {'question':question , 'answers':search2,'form':form})





