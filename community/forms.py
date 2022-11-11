from django import forms
from community.models import Column

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = "__all__"
