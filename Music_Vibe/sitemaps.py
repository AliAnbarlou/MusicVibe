from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from musics.models import Music_Class , Artist
from .views import Home_Page
class StaticIndexSitemap(Sitemap):
    def items(self):
        return [Home_Page]
    def location(self, item):
        return reverse(item)
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['About','Contact','devs']
    def location(self, item):
        return reverse(item)
class MusicViewSitemap(Sitemap):
    def items(self):
        return Music_Class.objects.all()#do the same for articles and artists
    
class ArtistViewSitemap(Sitemap):
    def items(self):
        return Artist.objects.all()#do the same for articles and artists

class GenersViewSitemap(Sitemap):
    def items(self):
        return [
            '/all',
            '/all/geners',
            '/all/geners/Pop',
            '/all/geners/Rap',
            '/all/geners/Rock',
            '/all/geners/Techno',
            '/all/geners/Phonk',
            '/all/geners/Classic',
            '/all/geners/Jazz',
            '/all/geners/Electronic',
            '/all/geners/Metal',
            '/all/geners/Traditional',
            '/all/geners/Remix',
            '/all/geners/Soundtrack',
            '/all/geners/Relaxing',
            '/danial-zarepour/',
            '/artists/',
            '/all/articles/',
        ]
    def location(self, item):
        return(item)