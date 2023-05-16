from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Make user ->> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# Create your models here.
class Profile(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ispokerpals = models.BooleanField(blank=False, default=False)
    city = models.CharField(default="Oldenzaal",max_length=150, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self): 
        return self.user.username


class PokerPalsSessions(models.Model):
    date = models.DateField(null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    time_delta = models.FloatField(blank=False)
    small_blind = models.FloatField(blank=False)
    big_blind = models.FloatField(blank=False)
    seven_two_off = models.BooleanField(blank=False)
    straddle = models.BooleanField(blank=False)
    session_id = models.IntegerField(blank=True)

    def __str__(self):
        return f"Session {self.session_id} at {self.date}"
    

class UserSessions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_roll = models.FloatField(blank=False)
    added_chips = models.FloatField(blank=False)
    end_roll = models.FloatField(blank=False)
    session = models.ForeignKey(PokerPalsSessions, on_delete=models.CASCADE)
    approved = models.BooleanField(blank=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by', null=True, blank=True)

    def __str__(self):
        return f"Session {self.session.session_id} by {self.user.username}"


def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(user=instance)

