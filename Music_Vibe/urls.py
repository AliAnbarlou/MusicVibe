"""
URL configuration for Music_Vibe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import error_404 , error_500
from django.views.generic.base import TemplateView
from .sitemaps import StaticViewSitemap , MusicViewSitemap , GenersViewSitemap , StaticIndexSitemap , ArtistViewSitemap
from django.contrib.sitemaps.views import sitemap
error_404 = 'Music_Vibe.views.error_404'
error_500 = 'Music_Vibe.views.error_500'
sitemaps = { "Index":StaticIndexSitemap ,'static' : StaticViewSitemap, "Musics":MusicViewSitemap , "Geners":GenersViewSitemap ,"Artists":ArtistViewSitemap}
admin.site.site_header = "Music Vibe"
urlpatterns = [
    path('log_in/HelloAdmin/', admin.site.urls),
    path('all/',include("all.urls")), #Show all the music
    path('about/', views.About, name='About'), #Show About us page
    path('artists/', views.Artists, name='artists'), #Show All Artists
    path('contact-us/', views.Contact, name='Contact'), #Show Contact us page
    path('artists/<int:artist_id>/', views.artist_details_view, name='artist_details'),  # Show Artist Details    path('contact-us/', views.Contact, name='Contact'), #Show Contact us page
    path('', views.Home_Page, name='Home'), #Show Home page
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('devs/', views.devs, name='devs'), #Show Home page
    path("danial-zarepour/", views.dani, name='dani'), #Show dani is gay
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("sitemap.xml/", sitemap,{'sitemaps':sitemaps}, name='django.sitemaps.views.sitemap'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)