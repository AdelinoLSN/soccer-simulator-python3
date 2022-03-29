import helpers.helper as helper
from classes.match import Match

def main():
    team_a, team_b = helper.get_teams()
    print (str(team_a)+' x '+str(team_b))
    match = Match(team_a, team_b)
    match = match.play()
    print (match)
    return match

main()