from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest
# Create your views here.


class HomepageView(View):
    template_name = 'home/base.html'

    def get(self, request: HttpRequest):
        return render(request, self.template_name)
