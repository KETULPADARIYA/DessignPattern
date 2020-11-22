# event broker (observer)
# command CQS (command Query Seperation)
from abc import ABC
from enum import Enum


class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args,**kwargs)


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self,sender,query):
        self.queries(sender, query)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:

    def __init__(self,creature_game,what_to_query,default_value):
        self.value = default_value
        self.creature_game = creature_game
        self.what_to_query = what_to_query



class CreatureModifier(ABC):
    def __init__(self,game,creature):
        self.game = game
        self.creature =creature
        self.game.queries.append(self.handle)

    def handle(self,sender,query):
        pass


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)

class DoubleAttackModifier(CreatureModifier):
    def handle(self,sender,query):
        if sender.name == self.creature.name and query.what_to_query ==  WhatToQuery.ATTACK:
            query.value *=2





class Creature:

    def __init__(self, game, name, attack, defense):

        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense
        self.game = game


    @property
    def attack(self):
        q = Query(self.name,WhatToQuery.ATTACK,self.initial_attack)
        self.game.perform_query(self,q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name,WhatToQuery.DEFENSE,self.initial_attack)
        self.game.perform_query(self,q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


if __name__ == '__main__':
    game = Game()
    gobline = Creature(game,"Strong Goblin",2,2)
    print(gobline)
    with DoubleAttackModifier(game,gobline):
        print(gobline)
    print(gobline)