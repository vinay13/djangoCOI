from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from appy.models import Photo
from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
	

def index(request):	
    

    posts_list=Photo.objects.all()
    paginator = Paginator(posts_list, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        photos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)


    return render_to_response('appy/index.html',{
	'photos':photos,
	'sidephotos':Photo.objects.all().order_by('?')[:8],},
	context_instance=RequestContext(request))


def show(request,slug):
    b=Photo.objects.all()	
    show=get_object_or_404(Photo,slug=slug)	
    return render_to_response('appy/type.html',{
	 'photos':Photo.objects.filter(title=show),
	 'sidephotos':Photo.objects.all().order_by('?')[:4],
    })	



	
# Create your views here.
