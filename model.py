from tinydb import TinyDB, Query


class Player:

    def __init__(self, lastname='', firstname='', age='', birthday='', gender='', rank=''):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    def serialize(self):
        return{
            'lastname': self.lastname,
            'firstname': self.firstname,
            'age': self.age,
            'birthday': self.birthday,
            'gender': self.gender,
            'rank': self.rank
        }


class Tournament:
    def __init__(self, name='', place='', date='', rounds='4', touring='', players='', type='', description=''):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.touring = touring
        self.players = players
        self.type = type
        self.description = description

    def serialize(self):
        return{
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'rounds': self.rounds,
            'touring': self.touring,
            'players': self.players,
            'type': self.type,
            'description': self.description
        }


class Round:

    def __init__(self, match, number, starttime, endtime):
        self.match = match
        self.number = number
        self.starttime = starttime
        self.endtime = endtime

    def serialize(self):
        return{
            'match': self.match,
            'number': self.number,
            'starttime': self.starttime,
            'endtime': self.endtime

        }

