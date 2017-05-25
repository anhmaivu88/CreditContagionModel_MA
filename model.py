import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from agents.bank import Bank

class CreditContagionModel(Model):

    ### To do
    def __init__(self):
        self.name = "Credit Contagion Model"


    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        if self.verbose:
            print([self.schedule.time,
                   self.schedule.get_breed_count(Bank)])

    def run_model(self, step_count=200):
        if self.verbose:
            print('Initial number banks: ',
                  self.schedule.get_breed_count(Bank))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number banks: ',
                  self.schedule.get_breed_count(Bank))