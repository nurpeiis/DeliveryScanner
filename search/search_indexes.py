import datetime
from haystack import indexes
from search.models import Pricedata
#script that is responsible to assign search indexes
class DeliverOptimalIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.Charfield(document=True, use_template=True, template_name="search/deliverOptimal_text.txt")

    def get_model(self):
        return Pricedata
    
    def index_queryset(self, using=None):
        #Used when the entire index for model is updated
        return self.get_model().objects.all()