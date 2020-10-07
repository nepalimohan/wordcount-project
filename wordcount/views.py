from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext= request.GET['Fulltext']
    totalwords = fulltext.split()
    totalcount = {}
    for words in totalwords:
        if words in totalcount:
            #increase
            totalcount[words] += 1
        else:
            totalcount[words] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(totalwords), 'totalcount': totalcount})

def About(request):
    return render(request, 'about.html')