from django.urls import include,  path
from search.views import HomeView, ResultView

app_name = 'search'
urlpatterns = [
    path('', HomeView.as_view(), name = 'home' ), 
    path('result/', include('haystack.urls'))
    ]