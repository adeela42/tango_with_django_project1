from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index (request):

    #query the database for a list of ALL categories stores
    #order the categories by number of likes in descending order
    #retrieve the top 5 only
    #place the list in our context_dict dictionary which will be passed to the template engine

    category_list = Category.objects.order_by('-likes')[:5]

    #construct a dictionary to pass to the template engine as its context
    #note the key bold message is the same as {{bold message in the template
    context_dict = {'categories': category_list}

    #return a rendered response to send to the client
    #make use of a shortcut function to our lives easier
    #note the first parameter is the template we wish to use

    return render(request, 'rango/index.html', context_dict)

def about (request):
    return HttpResponse("Rango says here is the About page <br/> Back to the <a href='/rango/'>Index</a> page")


def category(request, category_name_slug):

    #create a context dictionary to pass to the template engine
    context_dict = {}

    try:
        #Can we find a category with the given name?
        #if we can't then raise an exception
        #this is done using the .get method
        category= Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        #retrieve all of the associated pages
        #filter returns 1 model instance
        pages = Page.objects.filter(category=category)

        #add our results to the context diot
        context_dict['pages'] = pages

        #also add the category the pages belong to, to the category dictionary
        context_dict['category'] = category

    except Category.DoesNotExist:
        #this code is invoked if we cannot find the specific category
        #just pass
        pass

    #render the response
    return render(request, 'rango/category.html', context_dict)