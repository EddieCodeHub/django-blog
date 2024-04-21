from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    A form for users to request collaboration.

    **Fields**
    - name: the user's name.
    - email: the user's email.
    - message: the collaboration request message.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')