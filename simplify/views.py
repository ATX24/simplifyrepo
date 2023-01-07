from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from simplify.simModel import *

class NewTextForm(forms.Form):
    text = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder': 'URL', 'style': 'width: 500;', 'class': 'form-control'}))
    sentences = forms.ChoiceField(label = '', choices = [(x, x) for x in range(1, 10)])


class NewTextForm2(forms.Form):
    text = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder': 'Text', 'style': 'width: 500; length: 20;', 'class': 'form-control'})) 
    sentences = forms.ChoiceField(label = '', choices = [(x, x) for x in range(1, 10)])



# Create your views here.

def index(request):
    request.session['message'] = ' '
    request.session['fullText '] = ' ',
    request.session['simText'] = ' ',
    request.session['sentences'] = 0
    


    # Check if method is POST
    
    if request.method == "POST":

        request.session['noURL'] = True

        # Take in the data the user submitted and save it as form
        if 'form1' in request.POST:
            print('form1 selected')
            form = NewTextForm(request.POST)
            request.session['noURL'] = False

        elif 'form2' in request.POST:
            print('form2 selected')
            form = NewTextForm2(request.POST)
            request.session['noURL'] = True
 
        

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the text from the 'cleaned' version of form data
            rec = form.cleaned_data["text"] 
            sen = form.cleaned_data["sentences"]
            if (rec.__contains__('https://') or request.session['noURL'] == True):
                request.session['fullText']  = rec
                request.session['sentences'] = sen
                return HttpResponseRedirect(reverse("simplify:ans"))

            else:
                request.session['message'] = 'Make sure to use a proper web address (Include https:// and .com)'
                return render(request, "simplify/index.html", {
                    "form": NewTextForm(),
                    "form2": NewTextForm2(),
                    "message": request.session['message']
                })
                
        
        else:
            # If the form is invalid, re-render the page with existing information.
            message = ' '
            return render(request, "simplify/index.html", {
                "form": NewTextForm(),
                "form2": NewTextForm2(),
                "message": request.session['message']
            })

    return render(request, "simplify/index.html", {
        "form": NewTextForm(),
        "form2": NewTextForm2(),
        "message": request.session['message']
    })


def ans(request):
    f = request.session['fullText']
    a = request.session['simText']
    s = request.session['sentences']

    print(f)
    print(s)

    if(f.__contains__('https://')):
        a = simModel.getSummaryURL(f, s)
    else:
        a = simModel.getSummary(f, s)

    return render(request, 'simplify/answer.html', {
        'full': f[0:300] + '...',
        'ans': a
    })


def about(request):
    return render(request, "simplify/about.html")



