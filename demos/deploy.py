from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
import sys

def main(source, name):
    # Constellation
    HOST = '127.0.0.1'
    PORT = 8100

    # deploy the contract to the network
    api = LedgerApi(HOST, PORT)
    # api = LedgerApi(network='alphanet')

    # Create keypair for the contract owner
    owner = Entity()
    owner_addr = Address(owner)
    # print(owner_addr)

    # Need funds to deploy contract
    api.sync(api.tokens.wealth(owner, 20000))

    # Create contract
    contract = Contract(source, owner)

    # Deploy contract
    api.sync(api.contracts.create(owner, contract, 10000))

    # Save the contract to the disk
    with open('sample.contract', 'w') as contract_file:
        contract.dump(contract_file)

    # Save the contract owner's private key to disk
    with open('owner_private.key', 'w') as private_key_file:
        owner.dump(private_key_file)

    print(f"Contract {name}.etch has successfully been deployed.")


if __name__ == '__main__':
    # Loading contract
    if len(sys.argv) == 2:
        demo = sys.argv[1]
        if demo == 'pet':
            filepath = "pet-shop/adoption"
        else:  # 'soa'
            filepath = "simple-open-auction/auction"
        with open(f"{filepath}.etch", 'r') as file:
            contract_text = file.read()
        main(contract_text, filepath)
    else:
      print("Print input wither 'pet' or 'soa' for contract to deployed.")
      exit(-1)
