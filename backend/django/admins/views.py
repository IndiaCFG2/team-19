from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from admins.forms import PolicyCreationForm
from .serializers import PolicyCreationSerializer
from .models import PolicyCreation

def create_policy(request):
    if request.method == 'POST':
        form = PolicyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Policy created Succesffuly")
    else:
        form = PolicyCreationForm()
    return render(request, 'policy.html', {
        'form': form,
    })


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = PolicyCreation.objects.all().order_by('policyname')
    serializer_class = PolicyCreationSerializer