from django import forms
from .models import Profile
from .models import PokerPalsSessions
from .models import UserSessions
from django.contrib.auth.models import User


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class SessionForm(forms.ModelForm):
    class Meta:
        model = UserSessions
        fields = ("user", "start_roll", "added_chips", "end_roll", "session", "approved")

    def __init__(self, *args, **kwargs):     
        super(SessionForm, self).__init__(*args, **kwargs)
        #self.fields['approved'].disabled = True
        self.fields['approved'].initial = False

