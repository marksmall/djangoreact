import logging

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings

import os


class FrontendAppView(TemplateView):
    template_name = 'index.html'

    # def get(self, request):
    #     try:
    #         with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
    #             return HttpResponse(f.read())
    #     except FileNotFoundError:
    #         logging.exception('Production build of app not found')
    #         return HttpResponse(
    #             """
    #             This URL is only used when you have built the production
    #             version of the app. Visit http://localhost:3000/ instead, or
    #             run `yarn run build` to test the production version.
    #             """,
    #             status=501,
    #         )


# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.


# def index(request):
#     return HttpResponse("I am flooder")
