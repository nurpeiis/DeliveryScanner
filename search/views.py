from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Pricedata

from django.shortcuts import render_to_response
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        query = request.GET.get("get")
        qs = Pricedata.objects.all()
        if query is not None:
            qs = qs.filter( Q(dishname_icontains=search_query) | Q(restaurant_icontains=search_query) )
        return render(request, self.template_name, {'results': qs} )
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
    