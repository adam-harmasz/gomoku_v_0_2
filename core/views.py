from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(LoginRequiredMixin, View):
    """Home View class"""
    def get(self, request):
        """GET method"""
        return render(request, 'core/home.html')


class AboutView(LoginRequiredMixin, View):
    """About View"""
    def get(self, request):
        """GET method"""
        return render(request, 'core/about.html')
