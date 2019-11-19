from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# load up the contract owner's private key
with open('owner_private.key', 'r') as private_key_file:
    owner = Entity.load(private_key_file)

# load up the deployed contract
with open('sample.contract', 'r') as contract_file:
    contract = Contract.load(contract_file)


### Interact with the contract #############################

# Printing message
print(contract.query(api, 'getAdopters'))

# Create keypair for new entity that interacts with contract
entity1 = Entity()
address1 = Address(entity1)
api.sync(api.tokens.wealth(entity1, 10000))
print(address1)


# Initialize tx fee
tok_transfer_amount = 200
fet_tx_fee = 100

# Execute smart contract5
pet_id = 10
result = api.sync(contract.action(api, 'adopt', fet_tx_fee, [entity1], pet_id))
print(result)
