from django.utils.html import strip_tags
from django import forms
from musics.models import Comment , Contact
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("writer", "comment_text")
    def clean_comment_text(self):
        comment_text = self.cleaned_data['comment_text']
        # Strip HTML tags
        comment_text_stripped = strip_tags(comment_text)
        # Check if the comment contains any links
        if 'http' in comment_text_stripped or 'www' in comment_text_stripped:
            raise ValidationError("Comments containing links are not allowed.")
        return comment_text

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'comment']