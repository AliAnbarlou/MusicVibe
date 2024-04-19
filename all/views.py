from django.shortcuts import render , get_object_or_404 , redirect
from musics.models import Music_Class , Comment , Artist
from musics.forms  import CommentForm
from taggit.models import Tag
from django.utils.html import strip_tags
from hitcount.views import HitCountDetailView

# Create your views here.

def all_home(request):
    data = Music_Class.objects.all()
    context = {
        "postsindb" : data,
    }
    return render(request, 'all/home.html',context=context)

class MyDetailView(HitCountDetailView):
    model = Music_Class
    template_name = 'all/details_view.html'
    count_hit = True  # Enable counting hits

    # Specify the URL keyword argument name for the primary key.
    pk_url_kwarg = 'blog_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_object()
        context['postsindb'] = data
        context['form'] = CommentForm()
        context['tags'] = data.genres.all()
        context['recent_posts'] = Music_Class.objects.filter(genres__in=data.genres.all()).order_by('-id')[:10]
        context['recent_posts_artist'] = Music_Class.objects.filter(artist=data.artist).order_by('-id')
        context['liked'] = False  # Pass the liked flag to the template
        return context

    def post(self, request, *args, **kwargs):
        if 'like_post' in request.POST:
            data = self.get_object()
            data.likes += 1
            data.save()
            return redirect('det', blog_id=self.kwargs['blog_id'])
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                data = self.get_object()
                existing_comment = Comment.objects.filter(article=data, writer=request.user)
                if not existing_comment.exists():
                    new_comment = form.save(commit=False)
                    new_comment.article = data
                    new_comment.comment_text = strip_tags(new_comment.comment_text)
                    new_comment.save()
                return redirect('det', blog_id=self.kwargs['blog_id'])

        return self.get(request, *args, **kwargs)
def search(request):
    if request.method == "POST":
        query_name = request.POST.get('q')
        if query_name:
            music_results = Music_Class.objects.filter(title__icontains=query_name)
            artist_results = Artist.objects.filter(name__icontains=query_name)
            if music_results.exists() or artist_results.exists():
                context = {
                    "music_results": music_results,
                    "artist_results": artist_results,
                }
                return render(request, 'search/search_results.html', context=context)
            else:
                return render(request, 'No_result.html')
        else:
            return render(request, 'No_result.html')
    else:
        return render(request, 'No_result.html')

def Genres(request):
    return render(request, 'all/Genres.html',{})
def posts_with_tag(request, tag_slug):
    data = Music_Class.objects.filter(genres__name__in=[tag_slug])
    posts = Music_Class.objects.filter(genres__name__in=[tag_slug])
    return render(request, 'all/Genre_User.html', {'posts': posts,"postsindb":data,'y':tag_slug})
