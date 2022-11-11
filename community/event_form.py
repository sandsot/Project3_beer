from django import forms
from community.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"