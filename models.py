from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'tomo'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 1

    endowment = c(100)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    print('defined foelds on the Group')


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0,max=Constants.endowment)
