from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from core import models
from . import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ExtractDataRedirectView(LoginRequiredMixin, View):
    """
    View which will unpack data from gomoku
    record file and pass it to serializer
    """

    def get(self, request):
        form = forms.GomokuRecordForm()
        return render(request, 'gomoku_app/gomoku_file_form.html', {'form': form})

    def post(self, request):
        form = forms.GomokuRecordForm(request.POST, request.FILES)
        user = User.objects.get(username=self.request.user)
        print('dupa', user)
        if form.is_valid():
            files = form.cleaned_data['file']
            models.GomokuRecordFile.objects.create(
                game_record_file=files,
                profile=user
            )
        return HttpResponseRedirect('/api/')


