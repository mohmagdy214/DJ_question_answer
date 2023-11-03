from django.shortcuts import render , redirect
from .models import Question , Answer
from .forms import AnswerForm , QuestionForm 
from django.views.generic import UpdateView, DeleteView

# Create your views here.

def question_list(request):
    search = Question.objects.all()
    questions = None
    if 'search_name' in request.GET:
        questions = request.GET['search_name']
        if questions:
            search = search.filter(question__icontains=questions)

    return render(request, 'forum/question_list.html', {'questions':search})



def question_new(request):
    if request.method == 'POST':
        form_q = QuestionForm(request.POST)
        if form_q.is_valid():
            myform_q = form_q.save(commit=False)
            myform_q.author = request.user
            myform_q.save()
            return redirect('/questions')
    else:
        form_q = QuestionForm()
    return render(request , 'forum/question_new.html' , {'form_q':form_q})



def question_detail(request,pk):
    question = Question.objects.get(id=pk)
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
    return render(request, 'forum/question_detail.html', {'question':question , 'answers':search2,'form':form})




class QuestionUpdate(UpdateView):
    model = Question
    fields = ['question','content','tags','created_at','author']
    success_url = '/questions'
    template_name = 'forum/question_edit.html'


class QuestionDelete(DeleteView):
    model = Question    
    success_url = '/questions'


class AnswerUpdate(UpdateView):
    model = Answer
    fields = ['answer']
    success_url = '/questions/questions_detail.html'
    template_name = 'forum/answer_edit.html'


class AnswerDelete(DeleteView):
    model = Answer    
    success_url = '/questions/questions_detail.html'