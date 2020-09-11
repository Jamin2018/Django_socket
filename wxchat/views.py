from django.shortcuts import render
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict
from wxchat.models import User

# Create your views here.
def index(request):
    context = {}
    context['hello'] = 'Hello TEST!'
    return render(request, 'index.html', context)


def getuserlist(request):

    l = []
    userdata = User.objects.all()
    for u in userdata:
        l.append(model_to_dict(u))
    data = json.dumps(l, ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8",)
