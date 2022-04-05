"""Forms files."""

# Django
from django import forms

# Local
from .models import Mail


class MailForm(forms.ModelForm):  # noqa D101

    def save(self, commit=True):  # noqa D102
        return super().save()

    class Meta:  # noqa D106
        model = Mail
        fields = ['email']
