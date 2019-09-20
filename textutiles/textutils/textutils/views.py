# i have created this website-aditi
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
 #   return HttpResponse("hello")

#def about(request):
 #   return HttpResponse("about hii")

#def index(request):
    #return HttpResponse('''Home <br><a href="http://127.0.0.1:8000/removepunc">remove</a><br><a href="http://127.0.0.1:8000/capitalizefirst">cap</a> <br><a href="http://127.0.0.1:8000/newlineremove">newlinw</a> <br><a href="http://127.0.0.1:8000/spaceremove">space</a><br><a href="http://127.0.0.1:8000/charcount">char</a>''')

# def new(request):
#     params = {'name':'aditi','place':'jaipur'}
#     return render(request,'index.html', params)

# def removepunc(request):
#     #get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #analyse the text
#     return HttpResponse("remove punc")
#     #return HttpResponse('''remove punc <br><a href="http://127.0.0.1:8000/">back</a>''')
#
# # def capitalizefirst(request):
# #     return HttpResponse('''capitalize first <br><a href="http://127.0.0.1:8000/">back</a>''')
# #
# # def newlineremove(request):
# #     return HttpResponse('''new line first <br><a href="http://127.0.0.1:8000/">back</a>''')
# #
# # def spaceremove(request):
# #     return HttpResponse('''space remover <br><a href="http://127.0.0.1:8000/">back</a>''')
# #
# # def charcount(request):
# #     return HttpResponse('''charcount <br><a href="http://127.0.0.1:8000/">back</a>''')

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    capitalize = request.GET.get('capitalize', 'off')
    print(capitalize)
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #analyzed=djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        params = {'analyzed_text':analyzed, 'purpose':'Removed Puncuatation',}
        return render(request,'analyzer.html',params)

    elif(capitalize == "on"):
        analyzed=""
        for char in djtext:
                analyzed= analyzed+char.upper()
        params = {'purpose':'change into capital', 'analyzed_text':analyzed}
        return render(request, 'analyzer.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyzer.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyzer.html', params)

    else:
        return HttpResponse("ERROR")