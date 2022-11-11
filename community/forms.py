from django import forms
from community.models import Community

class Column(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"
