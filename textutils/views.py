from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyse(request):
  dtext= request.POST.get('texts' , 'default')
  removepunc = request.POST.get('removepunc' , 'off')
  fullcaps = request.POST.get('fullcaps' , 'off')
  newlineremover = request.POST.get('newlineremover' , 'off')

  if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analysed = ""
    for char in dtext:
        if char not in punctuations:
            analysed = analysed + char
    params = { 'purpose': 'Removed Punctuations' ,'analysed_text':analysed}
    dtext= analysed

  if(fullcaps=='on'):
    analysed = ""
    for char in dtext:
        analysed = analysed + char.upper()
    params = { 'purpose': 'TO UPPER CASE' ,'analysed_text':analysed}
    dtext= analysed

  if( newlineremover=='on'):
    analysed = ""
    for char in dtext:
        if char !="\n" and char != "\r":
         analysed = analysed + char
    params = { 'purpose': 'Removed New lines' ,'analysed_text':analysed}

  if(removepunc != 'on' and fullcaps!='on' and newlineremover!='on'):  
      return HttpResponse("Error")  
      
  return render(request,'analyse.html',params)