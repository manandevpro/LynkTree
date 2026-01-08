from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    #template_name = 'lynktree/link_list.html'
    #context_object_name = 'profiles'
    
class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']
    #template_name = 'lynktree/link_form.html'
    success_url = reverse_lazy('lynktree:link-list')
    
class LinkDeleteView(DeleteView):
    model = Link
    #template_name = 'lynktree/link_confirm_delete.html'
    success_url = reverse_lazy('lynktree:link-list')
    
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    return render(request, 'lynktree/profile.html', {'profile': profile, 'links': links})

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('lynktree:link-list')
