from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from users.models import Country

class CountryCreateView(CreateView):
    models = Country
    template_name = 'users/country_create.html'

#class ProfileDetailView(DetailView):
    #model = Profile