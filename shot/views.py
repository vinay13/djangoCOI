#from django.shortcuts import render
#from shot.models import Category
from django.http import HttpResponse
#from shot.models import Page
from django.core.paginator import Paginator
from django.template import RequestContext

from django.core.paginator import Paginator
from shot.models import Page, Category
from django.shortcuts import render_to_response, get_object_or_404




def index(request):
   
    posts_list = Page.objects.all()	
    paginator = Paginator(posts_list, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

   
    return render_to_response('shot/index.html',
        { 'posts' : posts,
	   'categories': Category.objects.all(),
		 },
        context_instance=RequestContext(request))	



#    return render_to_response('shot/index.html', {
#        'categories': Category.objects.all()[:5],
#        'pages': Page.objects.all()
#    })

def page(request, slug):   
    return render_to_response('shot/index.html', {
        'page': get_object_or_404(Page, slug=slug)
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pages_list=Page.objects.filter(category=category)
    paginator=Paginator(pages_list,2)

    try:
	page=int(request.GET.get('page','1'))
    except:
	page=1

    try:
	pages=paginator.page(page)
    except(EmptyPage,InvalidPage):
	pages=paginator.page(paginator.num_pages)				   

#    category = get_object_or_404(Category, slug=slug)
    return render_to_response('shot/category.html',
        { 'pages' : pages,
           'categories': Category.objects.all(),
                 },
        context_instance=RequestContext(request))

	

#    category = get_object_or_404(Category, slug=slug)
#    return render_to_response('shot/category.html', {
#         'categories': Category.objects.all()[:5],
#        'pages': Page.objects.filter(category=category)[:5]
#    })



#def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
#    category_list = Category.objects.all()
#    context_dict = {'categories': category_list}


    # Render the response and send it back!
#    return render(request, 'shot/index.html', context_dict)


#def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
#    context_dict = {}

#    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
#        category = Category.objects.get(slug=category_name_slug)
#        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
#        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
#        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
#        context_dict['category'] = category
#    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
#        pass

    # Go render the response and return it to the client.
#    return render(request, 'shot/category.html', context_dict)



