from django.shortcuts import render
from .models import Staff
from django.views.generic import ListView



# view for Company Staffs


class StaffList(ListView):
    model = Staff
    context_object_name = 'team'
    template_name='team.html'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_count'] = self.get_queryset().count()
        return context




