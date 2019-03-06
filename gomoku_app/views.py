from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView

from core import models
from . import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ExtractDataRedirectView(LoginRequiredMixin, View):
    """
    View which will unpack data from gomoku
    record file, then signal will create proper record file object
    """

    def get(self, request):
        form = forms.GomokuRecordForm()
        ctx = {
            'form': form
        }
        return render(request, 'gomoku_app/gomoku_file_form.html', ctx)

    def post(self, request):
        form = forms.GomokuRecordForm(request.POST, request.FILES)
        user = User.objects.get(username=self.request.user)
        if form.is_valid():
            file = form.cleaned_data['file']
            models.GomokuRecordFile.objects.create(
                game_record_file=file,
                profile=user,
                status='file'
            )
            return HttpResponseRedirect ('/home')
        ctx = {
            'form': form
        }
        return render(request, 'gomoku_app/gomoku_file_form.html', ctx)


class DownloadExtractDataRedirectView(LoginRequiredMixin, View):
    """
    View which will download and unpack data from gomoku
    record file, then signal will create proper record file object
    """

    def get(self, request):
        form = forms.GomokuRecordURLForm()
        ctx = {
            'form': form
        }
        return render(request, 'gomoku_app/gomoku_file_form.html', ctx)

    def post(self, request):
        form = forms.GomokuRecordURLForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=self.request.user)
            url = form.cleaned_data['url']
            models.GomokuRecordFile.objects.create(
                url=url,
                profile=user,
                status='url'
            )
            return HttpResponseRedirect('/home')
        ctx = {
            'form': form
        }
        return render(request, 'gomoku_app/gomoku_url_form.html', ctx)


class GameRecordListView(LoginRequiredMixin, ListView):
    """View displaying list of gomoku games"""
    # queryset = models.GomokuRecord.objects.all()
    template_name = 'gomoku_app/game_list.html'
    paginate_by = 15

    def get_queryset(self):
        user = self.request.user
        qs = models.GomokuRecord.objects.filter(profile=user)
        if qs.exists():
            return qs
        return models.GomokuRecord.objects.all()


class GameRecordDetailView(LoginRequiredMixin, DetailView):
    """View displaying list of gomoku games"""
    queryset = models.GomokuRecord.objects.all()
    template_name = 'gomoku_app/game_detail.html'


# class GameRecordDeleteView(LoginRequiredMixin, DeleteView):
#     """Delete game record View"""
#     queryset = models.GomokuRecord.objects.all()

