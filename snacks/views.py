from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack


class HomePageView(TemplateView):
    template_name = 'home.html'


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack