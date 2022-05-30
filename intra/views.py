import json
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from intra.models import Announcement, User

def is_author(user):
    ''' Function to check if user is allowed to create, add \
        and delete announcements '''

    return user.groups.filter(name='authors').exists() \
            or user.is_staff

@login_required
def dashboard(request):
    announcements = Announcement.objects.order_by('-created_at')[:3]
    pinned_announcements = Announcement.objects.filter(pinned=True)
    return render(request, 'intra/dashboard.html', \
        {
            'announcements':announcements,
            'pinned_announcements':pinned_announcements,
        })

@method_decorator(login_required, name='dispatch')
class UserView(generic.DetailView):
    model = User
    template_name = 'intra/user.html'

@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
    model = User
    template_name = 'intra/user_list.html'

    def get_queryset(self):
        users = User.objects.values_list(
            'id',
            'image',
            'first_name',
            'last_name',
            'department',
        )
        return json.dumps(list(users))

@method_decorator(login_required, name='dispatch')
class AnnouncementListView(generic.ListView):     
    model = Announcement   
    template_name = 'intra/announcement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = is_author(self.request.user)
        return context  

@method_decorator(login_required, name='dispatch')
class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title','description']
    success_url = reverse_lazy('announcements')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_at = datetime.now()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not is_author(request.user):
            raise PermissionDenied(request.user)                
        return super().dispatch(request, *args, **kwargs)   

@method_decorator(login_required, name='dispatch')
class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['title','description','pinned']
    success_url = reverse_lazy('announcements')

    def dispatch(self, request, *args, **kwargs):
        if not is_author(request.user):
            raise PermissionDenied(request.user)                
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = reverse_lazy('announcements')  

    def dispatch(self, request, *args, **kwargs):
        if not is_author(request.user):
            raise PermissionDenied(request.user)                
        return super().dispatch(request, *args, **kwargs) 