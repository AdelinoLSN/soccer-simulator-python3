import random
from classes.team import Team

def get_teams():
    team_a_name = input("Enter team A: ")
    team_a_overall = input("Enter team A overall: ")
    # team_a_name = "Brasil"
    # team_a_overall = "81"
    team_a = Team(team_a_name, team_a_overall)

    team_b_name = input("Enter team B: ")
    team_b_overall = input("Enter team B overall: ")
    # team_b_name = "Alemanha"
    # team_b_overall = "93"
    team_b = Team(team_b_name, team_b_overall)

    print()

    return team_a, team_b

def get_ball_possession_list(match):
    overall_a = int(match.team_a.overall)
    overall_b = int(match.team_b.overall)
    while (overall_a + overall_b) < 200:
        overall_a *= 2
        overall_b *= 2

    ball_possession_team_a = overall_a
    ball_possession_team_b = overall_b

    ball_possession_list_a = ['a' for x in range(ball_possession_team_a)]
    ball_possession_list_b = ['b' for x in range(ball_possession_team_b)]
    ball_possession_list = ball_possession_list_a + ball_possession_list_b
    random.shuffle(ball_possession_list)
    ball_possession_list = ball_possession_list[:200]

    return ball_possession_list