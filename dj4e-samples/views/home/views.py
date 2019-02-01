from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

# Create your views here.

def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)

def danger(request) :
    response = """<html><body>
    <p>Your guess was """+request.GET['guess']+"""</p>
    </body></html>"""
    return HttpResponse(response)

def game(request) :
    response = """<html><body>
    <p>Your guess was """+escape(request.GET['guess'])+"""</p>
    </body></html>"""
    return HttpResponse(response)

def bounce(request) :
    return HttpResponseRedirect('https://www.dj4e.com/lessons')

# https://docs.djangoproject.com/en/2.1/topics/class-based-views/
class MainView(View) :
    def get(self, request):
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)
