import random
import numpy as np

from mesa import Agent


# helper function
def repayAmount(STratio, borrowing):
    repayAmount = STRatio * borrowAmount * np.random.uniform(0.95, 1) + (
                                                                        1 - STRatio) * borrowAmount * np.random.uniform(
        0.2, 1)
    return repayAmount


def sizeScore(jAsset, bankAsset, indic):
    sizeScore = math.log(jAsset) - (math.log(bankAsset) * indic) / sum(indic)
    return sizeScore


def relationScore(relationScore, IBborrowing, newIBborrowing, mu=):
    if time == 0:
        if IBborrowing == 0:
            relationScore = 0
        else:
            relationScore = math.log(IBborrowing)
    else:
        if newIBborrowing == 0:
            relationScore *= (1 - mu)
        else:
            relationScore += math.log(newIBborrowing)
    return relationScore


def totalScore(sizeScore, relationScore):
    totalScore = omega * relationScore + (1 - omega) * sizeScore
    return totalScore


def lendingDecision(IBborrowing, newIBborrowing=0, mu=, jAsset, bankAsset, indic):
    relationScore = relationScore(IBborrowing, newIBborrowing, mu=)
    sizeScore = sizeScore(jAsset, bankAsset, indic)
    totalScore = totalScore(sizeScore, relationScore)
    lendingProb = 1 / (1 + alpha * math.exp(beta * totalScore))
    lendingDecision = np.random.choice([0, 1], size=1, p=[1 - lendingProb, lendingProb])
    return lendingDecision


def lendingAmount(avaiResource, askAmount, lower, upper):
    lendingPrefer = np.random.uniform(lower, upper) * avaiResource
    lendingAmount = min(askAmount, lendingPrefer)
    return lendingAmount


class bankAgent(Agent):
    '''
    A bank that lend, borrow in interbank market and update balancesheet
    '''

    def __init__(self, name, balanceSheet, IBborrowing, IBlending, parameter):
        self.name = name
        self.balanceSheet = balanceSheet
        self.IBlending = IBlending
        self.IBborrowing = IBborrowing
        self.parameter = parameter
        self.sizeScore =
        self.relationshipScore =
        self.totalScore =

    def otherBankSizeScore(self, model):

    def otherBankRelationScore

    def otherBankTotalScore

    def repay(self, model, jname):
        '''

        '''
        STratio = self.parameter[]
        borrowing = self.IBborrowing[jname]
        iname = self.name
        j = model.schedule.activatingAgents[jname]
        repayAmount = repayAmount(STratio, borrowing)
        self.IBborrowing -= repayAmount
        self.cash -= repayAmount
        j.IBlending -= repayAmount
        j.cash += repayAmount

    def borrowingTarget():
        assetGrowth =
        assetTarget =
        IBborrowingPct =
        borrowingTarget = assetTarget * IBborrowingPct

    def avaiResource():

    def EAChange()

    def ask4loan(self, model, jname):
        j = model.schedule.activatingAgents[jname]

    def borrowingOrder(self, model):
        borrowingOrder = []
        for j in model.schedule.activatingAgents:

    def lend(self, model, jname):
        j = model.schedule.activatingAgents[jname]
        jAsset = j.asset
        IBborrowing = self.
        bankAsset = self.model.bankAsset
        # self.model.bankAsset = [bank.asset for bank in model.schedule.activatingAgents]
        indic = [1 if x > 0 else 0 for x in self.IBborrowing]
        lendingDecision = lendingDecision(IBborrowing, newIBborrowing, jAsset, bankAsset, indic)
        if lendingDecision == 1:
            lendingAmount = lendingAmount(avaiResource, askAmount, lower, upper)
            self.cash -= lendingAmount
            self.IBlending += lendingAmount
            j.cash += lendingAmount
            j.IBborrowing += lendingAmount
            self.avaiResource -= lendingAmount
            j.askAmount -= lendingAmount
            self.relationScore +=

    def depositChange(self):
        growth = self.parameter[]
        change = self.deposit(math.exp(growth) - 1)
        self.deposit += change
        self.cash += change

    def externalAssetChange(self, change):
        growth =
        change = self.externalAsset * (math.exp(growth) - 1)
        self.externalAsset += change
        self.cash -= change

    def equityChange(self):
        growth =
        change =
        self.equity += change
        self.cash += change

    def bankrupt()

    def stage1(self):
        '''
        A model step. At stage 1, borrowing banks repay part of their loan to lending banks
        '''
        otherActivatingBanksName = self.model.banksName
        model = self.model
        for jname in otherActivatingBanksName:
            self.repay(self, model, jname)

    def stage2:
        '''
        At stage 2, banks borrow and lend in the interbank market
        '''
        askBanks =
        for j in askBanks:
            j.lend(j, j.model, self.name)

    def stage3:
        '''
        At stage 3, banks update other entries of the balance sheet
        '''
        self.depositChange()
        self.equityChange()


class bankAgent(Agent):
    '''
    A bank that lend, borrow in interbank market and update balancesheet
    '''

    def __init__(self, balanceSheet, IBborrowing, IBlending, parameter):
        super().__init__(ID, model)
        self.balanceSheet = balanceSheet
        self.IBlending = IBlending
        self.IBborrowing = IBborrowing
        self.parameter = parameter
        self.cash =
        self.totalIBlending =
        self.externalAsset =
        self.deposit =
        self.totalIBborrwing =
        self.equity =
        self.STlendRatio =
        self.STborrowRatio =
        self.asset = self.cash + self.totalIBlending + self.externalAsset
        self.liability = self.asset
        self.scoreRelation = [math.x if x > 0 else 0 for x in self.IBborrowing]
        # other banks: list các bank trừ bank i
        self.otherBanks = model.schedule.agents

    def getIBlendingij(self, model, jname):

    def getIBborrowingij(self, model, jname):

    def repayAmounts(self, model, jname):
        # Calculate the amount of money paid to a particular other bank at stage 1
        j
        borrowAmount = self.IBborrowing[j]

        repayAmount = self.STborrowRatio * borrowAmount + (1 - self.STborrowRatio) * borrowAmount * 25 %

    def sizeScore(self, model):
        # Take j bank from bank list
        j =

        # Take input j Asset
        jAsset = j.asset
        # list of all banks' asset
        bankAsset = [bank.asset for bank in model.schedule.agents]
        # List of all banks' asset except bank i

        # indicator function
        indic = [1 if x > 0 else 0 for x in self.IBborrowing]

        sizeScore = math.log(jAsset) - (math.log(bankAsset) * indic) / sum(indic)

    def repay(self):
        otherBanks =
        for bank in otherBanks:
            repayAmount = repayAmount(self, model, otherBank)

            iname =
            jname =
            if self.Cash >= repayAmount:
                self.Cash -= repayAmount
                self.IBborrowing[jname] -= repayAmount
                otherBank.IBlending[iname] -= repayAmount
            if else:

    def targetCalculation(self):
        depositTarget =
        equityTarget =
        EATarget =

    def borrowingTarget(self)

    def relationScore(self, bankj, change):
        j =
        relationScore = self.relationScore[j]
        relationScore += change

    def totalScore(sizeScore, relationScore):
        totalScore = omega * relationScore + (1 - omega) * sizeScore
        return totalScore

    def lendingprob(totalScore):
        lendingprob = 1 / (1 + alpha * math.exp(beta * totalScore))

    def borrowAmount(self):
        avaiResource =
        asking =
        borrowAmount = min(avaiResource *)

    def amountLending

    def borrow(self):

    def lend(self):

    def set2zero(self):
        self.balanceSheet = 0
        self.IBborrowing = 0
        self.IBlending = 0
        self.liability = 0
        self.cash = 0
        self.totalIBborrwing = 0
        self.totalIBlending = 0
        self.deposit = 0
        self.externalAsset = 0
        self.equity = 0

    def bankruptBehavior(self, model):
        IBreturnrate =
        for j in otherBanks:
            jname = j.name
            iname = self.name
            payback = IBreturnrate * j.IBborrowing[iname]
            self.cash += payback
            self.equity -=
            self.IBlending = 0

            if j.cash < IBreturnrate * j.IBborrowing[i]:
                j.bankruptBehavior()
            else:
                j.IBborrowing[i] = 0
                j.cash -= IBreturnrate * j.IBborrowing[i]

        EAreturnrate =
        EAsellingValue = EAreturnrate * self.externalAsset
        self.externalAsset = 0
        self.cash += EAsellingValue
        if self.cash < self.deposit:
            set2zero()
        else:
            self.cash -= self.deposit
            if self.cash > self.totalIBlending:
                self.cash -= self.totalIBlending
                self.set2zero()
                for j in otherBanks:
                    j.IBborrowing[i] = 0

    def externalAssetChange(self, change):
        growth =
        change = self.externalAsset * (math.exp(growth) - 1)
        self.externalAsset += change
        self.cash -= change

    def depositChange(self, change):
        growth =
        change = self.deposit(math.exp(growth) - 1)
        self.deposit += change
        self.cash += change

    def equityChange(self):
        growth =
        change =
        self.equity += change
        self.cash += change

    def update(self):

    def stage1(self):
        '''
        A model step. At stage 1, borrowing banks repay part of their loan to lending banks
        '''

    def stage2
        '''
        At stage 2, banks borrow and lend in the interbank market
        '''

    def stage3
        '''
        At stage 3, banks update other entries of the balance sheet
        '''

