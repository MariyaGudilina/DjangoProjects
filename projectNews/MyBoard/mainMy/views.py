from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.core.mail import send_mail
# Create your views here.
from datetime import datetime
# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView


class UserTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

