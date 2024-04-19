from django.contrib import admin
from . models import Music_Class , Comment , Contact , Artist 
# Register your models here.

class Comment_inline(admin.StackedInline):
    model = Comment
    extra = 0 #empty comments
    """
    This class shows comments for each post
    """

class ArticleAdmin(admin.ModelAdmin):
    inlines = [Comment_inline]

admin.site.register(Music_Class , ArticleAdmin)   
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Artist)