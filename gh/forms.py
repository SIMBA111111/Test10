from django import forms


class GettingDataFromGithubForm(forms.Form):
    username = forms.CharField()