import random

class Team:
    def __init__(self, name, overall):
        self.name = name
        self.overall = int(overall)

    def __str__(self):
        return self.name+" ("+str(self.overall)+")"