from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .forms import UserRegisterForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('/api')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'accounts/registration_form.html', {'form': form})


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