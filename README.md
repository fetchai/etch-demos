# Etch dApplication demos
Etch version of popular tutorial dApps, including:

1) **Pet Shop** dApp from the Truffle tutorial: https://www.trufflesuite.com/tutorials/pet-shop
2) **Simple Open Auction** dApp from the Ethereum Vyper tutorial:
https://vyper.readthedocs.io/en/v0.1.0-beta.13/vyper-by-example.html#simple-open-auction

It may be migrated to etch-examples: https://github.com/fetchai/etch-examples


### Steps

1) Spin-up a local Fetch ledger
2) `git clone` a local copy
3) Run `cd etch-demos/demos`
4) Run `python deploy.py pet` to deploy pet-shop contract or `python deploy.py soa` to deploy simple-open-auction contract.
5) Use `interact.ipynb` Jupyter Notebook to test the interaction of the deployed contract(s).
