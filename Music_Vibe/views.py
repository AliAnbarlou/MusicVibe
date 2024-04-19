from django.shortcuts import render ,get_object_or_404
from musics.models import Music_Class , Contact, Artist
from musics.forms import ContactForm
from django.template.loader import get_template
from django.http import HttpResponseNotFound, HttpResponseServerError

def About(request):
    return render (request, 'about.html',{})

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def Home_Page(request):
    recent_posts = Music_Class.objects.order_by('-id')[:10]
    pop_posts = Music_Class.objects.filter(genres__name__in=['Pop']).order_by('-id')[:10]
    rap_posts = Music_Class.objects.filter(genres__name__in=['Rap']).order_by('-id')[:10]
    classic_posts = Music_Class.objects.filter(genres__name__in=['Classic']).order_by('-id')[:10]
    techno_posts = Music_Class.objects.filter(genres__name__in=['Techno']).order_by('-id')[:10]
    artist_results = Artist.objects.order_by('-id')[:10]
    return render (request, 'index.html',{'artist_results':artist_results,'recent_posts': recent_posts,'pop_posts': pop_posts,'rap_posts': rap_posts,'classic_posts': classic_posts,'techno_posts': techno_posts})



def Artists(request):
    artist_results = Artist.objects.all()  # Assuming Artist is your model
    return render(request, 'artists/all.html', {'artist_results': artist_results})

#model
def artist_details_view(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist_songs = Music_Class.objects.filter(artist=artist)
    return render(request, 'artists/artists.html', {'artist': artist, 'artist_songs': artist_songs})
def devs(request):
    return render (request, 'devs.html',{})

def error_404(request, exception):
    template = get_template('Errors/404.html')
    return HttpResponseNotFound(template.render())

def error_500(request):
    template = get_template('Errors/500.html')
    return HttpResponseServerError(template.render())

def dani(request):
    return render(request , 'dani.html',{})