from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import Http404


def index(request):
    return render(request, 'index.html')


def text(request, path: str):
    path = path.lower()
    if path == 'fuer':
        path = 'für'
    if path in ['denn', 'für', 'mich', 'ist', 'christus', 'das', 'leben', 'und', 'sterben', 'ein', 'gewinn']:
        return HttpResponse(path)
    else:
        raise Http404()


def denn(request):
    return HttpResponse("denn")


def für(request):
    return HttpResponse("für")


def mich(request):
    return HttpResponse("mich")


def ist(request):
    return HttpResponse("ist")


def christus(request):
    return HttpResponse("christus")


def das(request):
    return HttpResponse("das")


def leben(request):
    return HttpResponse("leben")


def und(request):
    return HttpResponse("und")


def sterben(request):
    return HttpResponse("sterben")


def ein(request):
    return HttpResponse("ein")


def gewinn(request):
    return HttpResponse("gewinn")
