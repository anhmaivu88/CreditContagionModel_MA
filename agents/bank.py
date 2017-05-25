import numpy as np

from mesa import Agent

class Bank(Agent):
    def __init__(self, params):
        self.name = params['name'] if 'name' in params else ''

