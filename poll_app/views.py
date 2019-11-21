from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):

    if request.method == 'POST':
        voto = request.POST['radio']
        question = Poll_questions.objects.get(id=voto)
        if question:
            question.votos += 1
            question.save()
        return redirect('index')
    
    polls = Poll.objects.all()
    
    return render(
        request=request,
        template_name='../templates/index.html',
        context={
            'polls': polls,
            }
        )
