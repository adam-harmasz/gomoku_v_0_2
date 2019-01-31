from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from core import models
from . import forms
from core.utils import extract_data_from_game_record_file


class ExtractDataRedirectView(View):
    """
    View which will unpack data from gomoku
    record file and pass it to serializer
    """

    def get(self, request):
        form = forms.GomokuRecordForm()
        return render(request, 'gomoku_app/gomoku_file_form.html', {'form': form})

    def post(self, request):
        form = forms.GomokuRecordForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['file']
            gomoku_file = models.GomokuRecordFile(game_record_file=files)
            gomoku_file.save()
            payload = extract_data_from_game_record_file(f'config/media/{gomoku_file.game_record_file}')
        return HttpResponse(payload['game_record'])


