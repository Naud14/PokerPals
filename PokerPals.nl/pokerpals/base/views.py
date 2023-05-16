from django.shortcuts import redirect, render
from datetime import *
from django.http import HttpResponse
from .models import PokerPalsSessions
from .models import UserSessions
from .models import Profile
from .calculations import *
from django.contrib.auth import login
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from django.db.models import Q
from .updates import * 
from .forms import NameForm
from .forms import *


# Create your views here.
def index(request):
    return render(request, "base/index.html")

@login_required
def sessionstats(request):
    sessions = PokerPalsSessions.objects.all()
    session_stats = all_session_stats()
    context = {"sessions": sessions, "session_stats":session_stats}
    return render(request, "base/sessionstats.html", context)

@login_required
def usersessionstats(request, session_id):
    user_session = UserSessions.objects.filter(session__session_id = session_id)
    context = {"session": user_session, "session_id" : session_id}
    return render(request, "base/usersession.html", context)

@login_required
def downloads(request):
    return render(request, "base/downloads.html")

@login_required
def userstats(request, user_name):
    played_sessions = UserSessions.objects.filter(user__username = user_name)
    user_stats = player_info(user_name)
    context = {"played_sessions" : played_sessions, "user_stats" : user_stats, "name":user_name}
    return render(request, "base/userstats.html", context)

@login_required
def userovervieuw(request):
    users = Profile.objects.filter(ispokerpals = True and  ~Q(user__username = 'admin'))
    context = {"users": users}
    return render(request, "base/userovervieuw.html", context)

@login_required
def leaderboard(request):
    leader_board_info = get_leaderboard_info()
    amount_of_players = Profile.objects.filter(ispokerpals = True and  ~Q(user__username = 'admin'))
    context = {"leaderboard_info": leader_board_info, "amount_of_players": len(amount_of_players)}
    return render(request, "base/leaderboard.html", context)

@login_required
def update_profile(request):
    #x = Profile.objects.get(user__username = request.user)
    #x.city = "Oldenzaaal"
    #x.save()
    form = NameForm()
    context = {"form": form}

    if request.method == "POST":
        name = request.POST.get("your_name")
        context["greeting"] = f"Welcome {name}!"

    return render(request, "base/updateprofile.html", context)

def session_update(requests):
    if requests.method == "POST":
        form = SessionForm(requests.POST)
        # form.fields['approved'].initial = False
        # find exisitng session
        session = requests.POST.get("session")
        does_session_exists = UserSessions.objects.filter(session = session).exists()
        if does_session_exists:
            form.add_error("session", "This session already exists!")
        
        if form.is_valid():
            # Save the form to the model
            form.save()
            return redirect("index")
    else: 
        form = SessionForm()

    context = {"form" : form}
    return render(requests, "base/sessionupdate.html", context)



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            # Log the user in and redirect to index 
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    
    context = {"form" : form}
    return render(request, "registration/register.html", context)
    
