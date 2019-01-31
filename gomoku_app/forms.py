from django import forms

from core import models
from . import views


class GomokuRecordForm(forms.ModelForm):

    class Meta:
        model = models.GomokuRecord