from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView


from .models import Question, Choice

# Create your views here.
# def index(request):
#    question_list = Question.objects.order_by('-id')[:2]
#    context ={
#        'question_list': question_list
#    }
#    return render(request, 'polls/index.html', context)
class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "question_list"

    def get_queryset(self):
       # """Return the last five published questions."""
        return Question.objects.order_by("-id")[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id )
#     return render(request, 'polls/results.html',{"question":question} )
class ResultsView(DetailView):
    model = Question
    template_name= 'polls/results.html'

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            "question": question,
            "error_message": "debes seleccionar una opcion"
        })