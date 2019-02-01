from django import forms

from core import models
from . import views


class GomokuRecordForm(forms.Form):
    """Form to upload game record file"""
    file = forms.FileField(widget=forms.FileInput())
