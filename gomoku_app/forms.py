from django import forms

from core import models
from . import views


class GomokuRecordForm(forms.Form):
    """Form to upload game record file"""
    file = forms.FileField(widget=forms.FileInput())


class GomokuRecordURLForm(forms.Form):
    """Form to pass url to the game record at playok.com"""
    file = forms.CharField()
