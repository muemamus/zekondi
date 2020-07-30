from django.shortcuts import render

"""
  This handles GET HTTP request to http://localhost:8080/
  or http://zekondi.herokuapp.com/

  It sends back  to the client the index webpage HTML file
  
"""




def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')