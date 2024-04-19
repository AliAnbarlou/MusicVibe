from django.urls import reverse , path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.all_home, name='all_page'),
    path('<int:blog_id>/', views.MyDetailView.as_view(), name="det"),#details_view.html
    path('detail/<int:blog_id>/', views.MyDetailView.as_view(), name='detail'),
    path('search/',view=views.search,name='search'),
    path("geners/", view=views.Genres, name="geners"),
    path('geners/<slug:tag_slug>/', views.posts_with_tag, name='posts_with_tag'),
    path('like/<int:blog_id>/', views.MyDetailView.as_view(), name='like_post'),

]
