import settings
from django.shortcuts import render_to_response
import assetmanager.models as AM

def dashboard(request):
    return render_to_response('dashboard.html', {})

