from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import Http404


def index(request):
    return render(request, 'index.html')


def text(request, path: str):
    path = path.lower()
    if path == 'fuer':
        path = 'für'
    path = path.split('.html')[0]
    if path in ['denn', 'für', 'mich', 'ist', 'christus', 'das', 'leben', 'und', 'sterben', 'ein', 'gewinn']:
        return render(request, path + '.html')
    else:
        raise Http404()


def geheimsatz(request):
    if request.method != 'POST':
        return HttpResponseRedirect('gewinn')

    if request.POST.get('text', '').lower() == 'brüder wissen dass leben in christus ist':
        EmailMessage('Done', 'The kids are done bro', to=['mail@christophroyer.com']).send()
        return render(request, 'finish.html')
    else:
        return render(request, 'failure.html')
