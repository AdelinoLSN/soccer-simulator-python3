from time import sleep
import random
import helpers.helper as helper

class Match:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = 0
        self.team_b_score = 0
        self.ball_possession = random.choice(['a', 'b'])

    def __str__(self):
        return str(self.team_a)+" "+str(self.team_a_score)+"x"+str(self.team_b_score)+" "+str(self.team_b)

    def play(self):
        match = self

        ball_possession_list = helper.get_ball_possession_list(match)
        
        match, ball_possession_list = match.playFirstTime(ball_possession_list)
        match = match.playSecondTime(ball_possession_list)

        return match

    def playFirstTime(self, ball_possession_list):
        match = self

        time = 0
        while time <= 45:
            if (time == 45):
                extra_time = 1
                while extra_time < random.randint(0, 5):
                    extra_time += 1
                    match = match.doPlay(ball_possession_list.pop(), time, extra_time)
                time = 46
            else:
                match = match.doPlay(ball_possession_list.pop(), time)
                time += 1

        return match, ball_possession_list

    def playSecondTime(self, ball_possession_list):
        match = self

        time = 46
        while time <= 90:
            if (time == 90):
                extra_time = 1
                while extra_time < random.randint(3, 10):
                    extra_time += 1
                    match = match.doPlay(ball_possession_list.pop(), time, extra_time)
                time = 91
            else:
                match = match.doPlay(ball_possession_list.pop(), time)
                time += 1

        return match

    def doPlay(self, ball_possession, time, extra_time = 0):
        sleep(0.2)
        match = self
        result = self.result()

        if (result == 'y' and ball_possession == 'a'):
            match.team_a_score += 1
            if (extra_time > 0):
                print("{}' {} - Goal for {}".format(str(str(time)+'+'+str(extra_time)).rjust(5, '_'), match, match.team_a.name))
            else:
                print("{}' {} - Goal for {}".format(str(time).rjust(5, '_'), match, match.team_a.name))
        elif (result == 'y' and ball_possession == 'b'):
            match.team_b_score += 1
            if (extra_time > 0):
                print("{}' {} - Goal for {}".format(str(str(time)+'+'+str(extra_time)).rjust(5, '_'), match, match.team_b.name))
            else:
                print("{}' {} - Goal for {}".format(str(time).rjust(5, '_'), match, match.team_b.name))
        elif (time % 5 == 0):
            if (extra_time > 0):
                print("{}' {}".format(str(str(time)+'+'+str(extra_time)).rjust(5, '_'), match))
            else:
                print("{}' {}".format(str(time).rjust(5, '_'), match))
        return match


    def result(self):
        seed = random.randint(1, 4)
        goal = ['y' for x in range(seed)]
        not_goal = ['n' for x in range(100)]
        chance = goal + not_goal
        random.shuffle(chance)

        return chance[0]