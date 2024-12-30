from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'services.html')

def network_design(request):
    return render(request, 'services/network design.html')

def fiber_optics_services(request):
    return render(request, 'services/fiber optics services.html')

def network_management(request):
    return render(request, 'services/network management.html')

def osp_insight(request):
    return render(request, 'services/osp insight.html')

def testing_and_terminations(request):
    return render(request, 'services/testing and terminations.html')

def manhole_placement(request):
    return render(request, 'services/manhole placement.html')