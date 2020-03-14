from django.shortcuts import render

# Create your views here.

def home01(request):
    return render(request, 'home01.html')

def result01 (request):
    text = request.GET['fulltext']
    textcount = len(text)
    divide = text.split()
    dic = {}
    for ch in divide:
        if ch in dic:
            dic[ch] +=1
        else:
            dic[ch] = 1
    return render(request, 'result01.html', {'text' : text, 'textcount' : textcount, 'dic' : dic, 'divide' : divide, 'ch' : ch})