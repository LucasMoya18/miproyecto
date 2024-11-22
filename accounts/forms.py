from django import forms
from accounts.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        models = Ticket
        fields = ['ticket_problema','ticket_detalles']