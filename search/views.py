from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from haystack.query import SearchQuerySet
from .models import Pricedata

from django.shortcuts import render_to_response
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
  
    """
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Pricedata.objects.filter(title__icontains=query)
        else:
            return Pricedata.objects.all()
            """
class ResultView(TemplateView):
    template_name = 'search/results.html'
    