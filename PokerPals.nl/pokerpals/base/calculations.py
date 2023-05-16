from .models import PokerPalsSessions
from .models import UserSessions
from .models import Profile
from django.db.models import Q


def player_info(user_name):
    # Calculate played sessions
    user_info = UserSessions.objects.filter(user__username = user_name)

    # Calculate played sessions
    played_sessions = len(user_info)

    # Calculate total stacks
    total_begin_stack = 0
    total_end_stack = 0
    total_added_chips = 0

    total_played_hours = 0
    total_session_profits = 0


    for session in user_info:
        total_begin_stack += session.start_roll
        total_end_stack += session.end_roll
        total_added_chips += session.added_chips

        total_played_hours += session.session.time_delta
        total_session_profits += session.end_roll - session.added_chips - session.start_roll

    # Calculate total profit and total lose


    # Calculate averages
    average_begin_stack = total_begin_stack / played_sessions
    average_end_stack = total_end_stack / played_sessions
    average_added_chips = total_added_chips / played_sessions
    average_session_profit = total_session_profits / played_sessions
    average_hour_profit = total_session_profits / total_played_hours

    player_stats_dictionary = {"played_sessions": played_sessions, "total_begin_stack":total_begin_stack, 
                               "total_end_stack":total_end_stack, "total_added_chips":total_added_chips,
                               "total_played_hours": total_played_hours, "total_session_profits":total_session_profits, 
                               "average_begin_stack":average_begin_stack, "average_end_stack":average_end_stack, 
                               "average_added_chips":average_added_chips, "average_session_profit":average_session_profit, 
                               "average_hour_profit": average_hour_profit}



    return player_stats_dictionary


def all_session_stats():
    played_sessions = len(PokerPalsSessions.objects.all())


    all_players = Profile.objects.filter(~Q(user__username = 'admin'))
    all_player_info_list = list()
    for player in all_players:
        if player.ispokerpals == True:
            all_player_info_list.append(player_info(player))
    
    # Total amounts
    total_played_money = 0
    total_begin_money = 0
    total_end_money = 0
    total_added_money = 0   

    for player in all_player_info_list:
        total_played_money += (player.get("total_begin_stack") + player.get("total_added_chips"))
        total_begin_money += player.get("total_begin_stack")
        total_end_money += player.get("total_end_stack")
        total_added_money += player.get("total_added_chips")


    # Average amounts
    average_played_money_per_session = total_played_money / played_sessions
    average_begin_money_per_session = total_begin_money / played_sessions
    average_end_money_per_session = total_end_money / played_sessions
    average_added_money_per_session = total_added_money / played_sessions

    session_stats_dictionary = {"total_played_money": total_played_money, "total_begin_money":total_begin_money, 
                                "total_end_money":total_end_money, "total_added_money":total_added_money, 
                                "average_played_money_per_session": average_played_money_per_session, 
                                "average_begin_money_per_session": average_begin_money_per_session, 
                                "average_end_money_per_session":average_end_money_per_session, 
                                "average_added_money_per_session":average_added_money_per_session, 
                                "total_played_sessions": played_sessions}

    return session_stats_dictionary

def get_leaderboard_info():
    leader_board_dictionary = dict()
    average_session_dictionary = dict()
    average_hour_dictionary = dict()

    users = Profile.objects.filter(ispokerpals = True and  ~Q(user__username = 'admin'))
    for user in users:
        user_info = UserSessions.objects.filter(user__username = user.user.username)
        played_sessions = len(user_info)

        total_played_hours = 0
        total_session_profits = 0

        for session in user_info:
            total_played_hours += session.session.time_delta
            total_session_profits += session.end_roll - session.added_chips - session.start_roll

        average_session_profit = total_session_profits / played_sessions
        average_hour_profit = total_session_profits / total_played_hours

        # leader_board_dictionary[str(user.user.username)] = {"average_session_profit": average_session_profit, "average_hour_profit" : average_hour_profit, "test" : "TESTJE"}
        average_session = {"result":  average_session_profit}
        average_hour = {"result" : average_hour_profit}
        
        average_hour_dictionary[str(user.user.username)] = average_hour
        average_session_dictionary[str(user.user.username)] = average_session


    sorted_session = sorted(average_session.items(), key=lambda x:x[1], reverse=True)
    sorted_hour = sorted(average_hour.items(), key=lambda x:x[1], reverse=True)

    leader_board_dictionary["average_session_dictionary"] = average_session_dictionary
    leader_board_dictionary["average_hour_dictionary"] = average_hour_dictionary
    
    return leader_board_dictionary

