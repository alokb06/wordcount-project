from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    text_content = request.GET['fulltext']
    text_content = text_content.strip()
    text_content = text_content.split(' ')
    count_text = len(text_content)
    worddictionary = {}
    for word in text_content:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html',{"fulltext":text_content,"count_text":count_text,'worddictionary':worddictionary.items()})


def about(request):
    return render(request, 'about.html')