from django.shortcuts import render
from django.views import generic
import requests
from gh import forms
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GettingDataFromGithub(generic.FormView):
    form_class = forms.GettingDataFromGithubForm
    template_name = "gh/gh-get-data.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            return render(request, template_name="gh/gh-post-data.html", context={'data': data})
        else:
            return render(request, template_name="gh/gh-post-data.html", )

