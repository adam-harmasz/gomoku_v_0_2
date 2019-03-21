"""Forms for uploading/downloading game records"""
from django import forms

from core.utils import check_domain


class GomokuRecordForm(forms.Form):
    """Form to upload game record file"""

    file = forms.FileField(widget=forms.FileInput(), required=True)


class GomokuRecordURLForm(forms.Form):
    """Form to pass url to the game record at playok.com"""

    url = forms.URLField(widget=forms.URLInput(), required=True)

    def clean_url(self):
        """
        Validating given url, only urls from kurnik.pl or playok.com
        domains are allowed
        """
        allowed_domains = ("https://www.kurnik.pl", "https://www.playok.com")
        url = self.cleaned_data["url"]
        print(check_domain(url))
        if check_domain(url) in allowed_domains and url[-3:] == "txt":
            return url
        raise forms.ValidationError(
            "Invalid url, only games from kurnik.pl" " or playok.com are allowed"
        )
