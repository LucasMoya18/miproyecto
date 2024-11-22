from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Ticket
from accounts.forms import TicketForm

@login_required
def home(request):
    return render(request, 'home.html')


def tickets(request):
    tickessss = Ticket.objects.all()
    return render(request,'tickets.html', {'salas': tickessss})

def crearTicket(request):
    formulario = TicketForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('tickets')
    return render(request, 'paginas/agregarTicket.html', {'formulario':formulario})