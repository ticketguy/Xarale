from django.shortcuts import render
from team.models import Staff
from feedback.models import Feedback, Count, Client


def index(request):
    staff_count = Staff.objects.count()  # Get the total number of staff
    return render(request, 'index.html', {'staff_count': staff_count})

def skills_view(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'index.html', {'feedback_list': feedback_list})


def counts_view(request):
    counts = Count.objects.all()
    return render(request, 'index.html', {'counts': counts})

def clients_view(request):
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients})

# contact views

def about(request):
    return render(request, 'about.html')



 