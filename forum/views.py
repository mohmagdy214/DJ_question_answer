from django.shortcuts import render
from .models import Question , Answer
# Create your views here.

def question_list(request):
    data = Question.objects.all()
    return render(request, 'forum/question_list', {'data':data})



def question_detail(request,question_id):
    question = Question.objects.filter(id=question_id)
    



    return render(request, 'forum/question_detail', {'question':question})





