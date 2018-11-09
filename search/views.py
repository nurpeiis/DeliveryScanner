from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from haystack.query import SearchQuerySet
# Create your views here.
class HomeView(TemplateView):
    template_name = 'search/index.html'
    #query = request.GET.get("q")
   
class ResultView(TemplateView):
    template_name = 'search/results.html'
    deliverQuery = SearchQuerySet().autocomplete(content_auto=request.GET.get('search_text',''))

    return render_to_response('search/results.html', {'deliver': deliver })