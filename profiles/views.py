from django.shortcuts import render, get_object_or_404

from .models import UserProfile

"""

  This handles GET HTTP request to http://localhost:8080/profiles or 
  http://zekondi.herokuapp.com/profiles

  It sends back  to the client to the user's profile inside HTML file.

"""

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)