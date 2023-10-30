from django.shortcuts import render
from .models import Question , Answer
from .forms import AnswerForm
# Create your views here.

def question_list(request):
    data = Question.objects.all()
    return render(request, 'forum/question_list', {'data':data})



def question_detail(request,question_id):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.question = question
            myform.save()
    else:
        form = AnswerForm()


    return render(request, 'forum/question_detail', {'question':question , 'answers':answers,'form':form})





