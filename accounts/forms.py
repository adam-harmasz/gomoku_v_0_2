from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    # Form for user registration with email, and user validation
    email = forms.EmailField()
    password = forms.CharField(required=True,
                               label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(required=True,
                                label='Repeat password',
                                widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        # username validation
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('The field cannot be empty')
        qs = User.objects.filter(username=username)
        if qs.exists():
            print('username')
            raise ValidationError(f'{username} already exists')
        return username

    def clean_email(self):
        # email validation
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Field cannot be empty')
        qs = User.objects.filter(email=email)
        if qs.exists():
            print('email')
            raise ValidationError(
                f'that email address {email} is already taken')

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if not password or not password2:
            raise forms.ValidationError('Both password fields cannot be empty')
        if password != password2:
            raise ValidationError('Passwords don\'t match')
