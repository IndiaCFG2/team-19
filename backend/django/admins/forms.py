from django import forms

from admins.models import PolicyCreation


class PolicyCreationForm(forms.ModelForm):
    class Meta:
        model = PolicyCreation
        fields = ('policyname', 'description')