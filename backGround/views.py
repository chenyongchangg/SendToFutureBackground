from django.shortcuts import render,HttpResponse
from . import models
import json
from django.http import JsonResponse
from django.core import serializers
from django.core.mail import send_mail
import time
import threading



# Create your views here.


def add(request):
    dto = models.Dto()

    dto. email = request.GET['email']
    dto.date = request.GET['date']
    dto.content = request.GET['content']
    dto.isPublic = request.GET['isPublic']
    dto.save()
    return  HttpResponse('你的信笺正通过时光隧道向你的未来飞去')


def getall(request):
    data = {}
    book = models.Dto.objects.all()
    data['list'] = json.loads(serializers.serialize("json", book))
    return JsonResponse(data)


def getnumber(request):
    send_mail('Subject here', 'This video is unavailable. Watch Queue Queue. Watch Queue Queue',
              'chenyongchangg@126.com',
              ['chenyongchanggg@126.com'], fail_silently=False)
    data = {}
    book = models.Dto.objects.last()

    #print (book.date)
    #print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    #data['list'] = json.loads(serializers.serialize("json", book))
    #return JsonResponse(data)
    if book.date.strftime('%Y-%m-%d')>time.strftime('%Y-%m-%d', time.localtime(time.time())):

        return HttpResponse('ok')
    else:
        return HttpResponse('this is over')


def send():
    while 1:
        book = models.Dto.objects.all()
        for item in book:
            if item.date.strftime('%Y-%m-%d')<time.strftime('%Y-%m-%d', time.localtime(time.time())) and item.isSend == False :
                send_mail('还记得曾经的信吗?', item.content,
                          'chenyongchangg@126.com',
                          [item.email], fail_silently=False)

                print(item.isSend)
                item.isSend = True
                item.save()


thread = threading.Thread(target=send)
thread.start()


