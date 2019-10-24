from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import VotoForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        voto = request.POST['radio']
        question = Poll_questions.objects.get(id=voto)
        if question:
            question.votos += 1
            question.save()
        return redirect('index')
    else:
        polls = Poll.objects.all()
        polls_questions = Poll_questions.objects.all()
        return render(
            request=request,
            template_name='../templates/index.html',
            context={
                'polls': polls,
                'polls_questions': polls_questions,
            }
        )

