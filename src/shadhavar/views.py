from django.shortcuts import render_to_response
import assetmanager.models as AM

def dashboard(request):
    #TODO: Fetch events and notifications
    return render_to_response('dashboard.html', {})

