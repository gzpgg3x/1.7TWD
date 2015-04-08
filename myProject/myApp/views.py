# from django.shortcuts import render

# def index(request):
#     render ("Hello World")

from django.http import HttpResponse
from django.shortcuts import render
from myApp.models import Category, Page

# def index(request):
#     return HttpResponse("Rango says hey there world!")

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'myApp/index.html', context_dict)