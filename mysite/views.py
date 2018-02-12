from django.views.generic.base import TemplateView
import datetime
from django.shortcuts import HttpResponse
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# def home(request):
#     now = datetime.datetime.now()
#     html = "<html><body>안녕하세요 %s.</body><html>" % now
#
#     return HttpResponse(html)

class Home(TemplateView):
    template_name = "home.html"



class UserRegister(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDone(TemplateView):
    template_name = "registration/register_done.html"