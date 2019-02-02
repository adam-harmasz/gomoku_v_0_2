from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm

User = get_user_model()


class RegisterView(View):
    """Class that handles registration process"""

    def get(self, request):
        """function handling GET method"""
        form = UserRegisterForm()
        return render(
            request,
            'accounts/registration_form.html',
            {'form': form})

    def post(self, request):
        """function handling POST method"""
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('asd')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/api')

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')


class UserProfileView(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/profile.html'
