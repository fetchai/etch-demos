from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
# from collections import defaultdict
from .contractinfo import ContractInfo
import datetime
import json


class Session:

    def __init__(self, network, port):
        self.network = network
        self.host = self.get_ip()
        self.port = port
        self.api = LedgerApi(self.host, self.port)
        self.contracts = {}  # {'name': ContractInfo}
        self.entities = {}  # {'name' : Entity}

    def get_ip(self):
        if self.network == 'localhost':
            return '127.0.0.1'
        else:
            return '127.0.0.1'

    def is_connected(self):
        try:
            self.api.tokens._current_block_number()
        except ConnectionError:
            return False
        else:
            return True

    def get_blockchain_info(self):
        success, data = self.api.tokens._get_json('status/chain', size=1)
        info = data['chain'][0]
        # info["Block #:"] = self.api.tokens._current_block_number()
        output = ""
        for k, v in info.items():
            if k == "timestamp":
                dt = datetime.datetime.fromtimestamp(v).strftime("%Y-%m-%d %H:%M:%S")
                v = f"{dt} GMT-4"
            output += f"{k.title()}: {v}  \n"
        return output

    # Deploying contract text on-chain, save both contract and owner entity
    def deploy(self, contract_name, contract_text, owner=Entity(),
               top_up=20000, tx_fee=10000):
        contract = Contract(contract_text, owner)
        self.api.sync(self.api.tokens.wealth(owner, top_up))
        self.api.sync(self.api.contracts.create(owner, contract, tx_fee))
        self.add_contract(contract_name, contract_text, contract, owner)
        self.add_entity(f"{contract_name}_owner", owner, top_up=0)

    def action(self, contract_name, func_name, tx_fee, signers, *params):
        name = self.contracts[contract_name]
        contract = name.contract
        return self.api.sync(contract.action(self.api, func_name, tx_fee,
                                             signers, *params))

    def query(self, contract_name, func_name):
        return self.contracts[contract_name].contract.query(self.api, func_name)

    # Get balance of either Entity pr Contract address
    def balance(self, address):
        return self.api.tokens.balance(address)

    # Storing and removing contract or entity "cookies" in session
    def add_contract(self, name, text, contract, owner):
        self.contracts[name] = ContractInfo(text, contract, owner)

    def remove_contract(self, name):
        del self.contracts[name]

    def add_entity(self, name, entity=None, top_up=10000):
        if entity is None:
            entity = Entity()
        self.entities[name] = entity
        self.api.sync(self.api.tokens.wealth(entity, top_up))
        # self.topup_entity(name, top_up)
        # self.contracts[contract_name].add_entity(entity_name, entity)

    def get_entity_info(self, name):
        entity = self.entities[name]
        address = Address(entity)
        info = {}
        info['Address'] = address
        info['Balance'] = self.balance(address)
        output = ""
        for k, v in info.items():
            output += f"{k.title()}: {v}  \n"
        return output

    # Refill balance of an entity
    def topup_entity(self, name, top_up=10000):
        entity = self.entities[name]
        self.api.sync(self.api.tokens.wealth(entity, top_up))

    def remove_entity(self, name):
        del self.entities[name]
        # self.contracts[contract_name].remove_entity(entity_name)
