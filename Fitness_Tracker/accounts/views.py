from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from Fitness_Tracker.accounts.forms import CustomUserForm, ProfileEditForm
from Fitness_Tracker.accounts.models import Profile


def home_view(request):
    return render(request, 'common/home.html')


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

class HomeView(TemplateView):
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/home_logged_in.html']
        return ['common/home.html']

def dashboard(request):
    return render(request, 'dashboard.html')


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileDetailsView(DetailView):
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile