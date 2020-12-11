# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def homePageView(request):
	return HttpResponse('<iframe src="https://trinket.io/embed/python/0481d0af9e?outputOnly=true&runOption=run&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>')