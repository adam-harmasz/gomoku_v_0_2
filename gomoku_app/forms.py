from django import forms

from core import models
from . import views


# class GomokuRecordForm(forms.ModelForm):
#     """Form to upload gomoku record file"""
#
#     class Meta:
#         model = models.GomokuRecordFile
#         fields = ('game_record_file',)
#         widgets = {'game_record_file': forms.FileInput()}


class GomokuRecordForm(forms.Form):
    """Form to upload game record file"""
    file = forms.FileField(widget=forms.FileInput())