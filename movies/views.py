from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Another(View):

    def get(self, request):
        return HttpResponse('This is another function inside class')


def index(request):
    return HttpResponse('First message from views')
