from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Poll

# Create your views here.
def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    firstPoll = Poll.objects.get(pk=1)
    # choices = firstPoll.choices.all()
    # print("these are the choices for all of hte polls", choices)
    data = {"results": list(polls.values("question", "created_by", "pub_date"))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = Poll.objects.get(pk=pk)
    data = {"results": {
        "question" : poll.question,
        "created_by": poll.created_by.username,
        "pub_date" : poll.pub_date
    }}
    return JsonResponse(data)

