from django.shortcuts import render,HttpResponse
from tips.models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request,'index.html')
@csrf_exempt
def search(request):
    word=request.POST['word']
    print word
    if word==''or word is None:
        entries=Entries.objects.filter(word=word)
    else:
        entries=Entries.objects.filter(word__startswith=word).order_by('datetime')
    word_list=[]
    words={}
    for entry in entries:
        word={'word':entry.word}
        word_list.append(word)
    return HttpResponse(json.dumps(word_list))
