from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.views import generic
# from .forms import TicketForm
import uuid
import phonenumbers

# Create your views here.
class EventsList(generic.ListView):
    queryset = Events.objects.all().order_by('-date')
    template_name = 'homie.html'


class EventDetail(generic.DetailView):
    model = Events
    template_name='event.html'

def single(request):
    return render(request, 'single.html')

def mobile_payment(request,ticket_id):
    return redirect()

