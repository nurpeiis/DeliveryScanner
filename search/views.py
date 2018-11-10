from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Pricedata

from django.shortcuts import render_to_response
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        query = request.GET.get("q")
        print(query)
        qs = Pricedata.objects.all().filter( Q(dishname__icontains=query) | Q(restaurant__icontains=query) )
        return render(request, self.template_name, {'results': qs} )

    