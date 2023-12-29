from .models import Comment, Contact
from django import forms


class CommentForm(forms.ModelForm):
    # From django blog walkthrough project

    """
    Form class for comment model, sets the input fields to body, which is
    displayed to the user.

    """
    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):
    # For custom model

    """
    Contact Form class for Contact model, sets the input fields to name, email,
    subjectand enquiry which is displayed to the user.
    displayed to the user.

    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'enquiry',)
