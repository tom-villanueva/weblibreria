from django.views.generic.edit import CreateView
from users.models import Country

class CountryCreateView(CreateView):
    models = Country