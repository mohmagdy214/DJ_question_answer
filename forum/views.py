from django.shortcuts import render
from .models import Question , Answer
# Create your views here.

def questions_list(request):
    data = Question.objects.all()
    return render(request, 'forum/questions_list', {'data':data})


