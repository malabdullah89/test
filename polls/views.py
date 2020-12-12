from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Poll


def index(request):
    template_name = 'index.html'
    polls = Poll.objects.all()
    context = {'polls': polls}

    return render(request, template_name, context)
