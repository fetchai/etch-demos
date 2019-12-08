from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
from collections import defaultdict
import re


class ContractInfo:

    def __init__(self, contract_text, contract, owner):
        # self.name = name
        self.contract = contract
        self.owner = owner
        # self.entities = defaultdict(list)
        self.funcs = defaultdict(list)
        self.get_functions(contract_text)

    def get_functions(self, contract_text):
        actionfunc = False
        queryfunc = False

        for line in contract_text.split('\n'):
            if line.strip() == "@action":
                actionfunc = True
            elif line.strip() == "@query":
                queryfunc = True
            elif actionfunc:
                funcname = line.replace('(', ' ').split(' ')[1]
                self.funcs['action'].append(funcname)
                actionfunc = False
            elif queryfunc:
                funcname = line.replace('(', ' ').split(' ')[1]
                self.funcs['query'].append(funcname)
                queryfunc = False

    # def add_entity(self, name, entity):
    #     self.entities[name].append(entity)
    #
    # def remove_entity(self, name):
    #     del self.entities[name]
