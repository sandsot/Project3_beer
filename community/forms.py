from django import forms
from community.models import Community

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = "__all__"
