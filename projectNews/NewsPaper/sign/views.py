from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

#import sys
#sys.path.append('..')

from news.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
        Author.objects.create(authorUser=user)
        return HttpResponseRedirect('/news/')


class UserDetail(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'sign/userDetail.html'
    form_class = BaseRegisterForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        return self.request.user


